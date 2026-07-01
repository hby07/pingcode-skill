#!/usr/bin/env python3
"""PingCode REST API generic wrapper (Python stdlib only).

Usage:
    python3 pingcode.py '{"method":"GET","path":"/v1/myself"}'
    python3 pingcode.py '{"method":"POST","path":"/v1/ship/work_items/{id}/comments","body":{"content":"hello"}}'
    python3 pingcode.py '{"method":"GET","path":"/v1/ship/products","params":{"page":1,"size":20}}'

Environment:
    PINGCODE_CLIENT_ID       Required – OAuth2 client ID
    PINGCODE_CLIENT_SECRET   Required – OAuth2 client secret
    PINGCODE_BASE_URL        Optional – default https://open.pingcode.com
    PINGCODE_TOKEN_CACHE     Optional – path to token cache file
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any, Dict, NoReturn
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DEFAULT_BASE_URL = "https://open.pingcode.com"
TOKEN_CACHE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), ".token_cache.json"
)
REQUEST_TIMEOUT = 15


def die(message: str, *, body: Any | None = None, exit_code: int = 1) -> NoReturn:
    payload: Dict[str, Any] = {"error": message, "exit_code": exit_code}
    if body is not None:
        payload["body"] = body
    print(json.dumps(payload, ensure_ascii=False))
    raise SystemExit(exit_code)


# ── .env file support ───────────────────────────────────────────────
_ENV_LOADED = False
_ENV_DATA: Dict[str, str] = {}


def _load_env_file() -> None:
    """Load .env file from script directory or skill root."""
    global _ENV_LOADED, _ENV_DATA
    if _ENV_LOADED:
        return
    _ENV_LOADED = True
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, ".env"),
        os.path.join(script_dir, "..", ".env"),
    ]
    for env_path in candidates:
        try:
            with open(env_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        key, _, value = line.partition("=")
                        key = key.strip()
                        value = value.strip().strip('"').strip("'")
                        if key and value:
                            _ENV_DATA[key] = value
        except FileNotFoundError:
            continue


def _env_get(key: str, default: str = "") -> str:
    """Get value from env var, falling back to .env file."""
    _load_env_file()
    return os.getenv(key, "").strip() or _ENV_DATA.get(key, default).strip()


def get_base_url() -> str:
    return _env_get("PINGCODE_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def get_credentials() -> tuple[str, str]:
    cid = _env_get("PINGCODE_CLIENT_ID")
    csec = _env_get("PINGCODE_CLIENT_SECRET")
    if not cid:
        die("PINGCODE_CLIENT_ID not found (set env var or put in .env file)")
    if not csec:
        die("PINGCODE_CLIENT_SECRET not found (set env var or put in .env file)")
    return cid, csec


# ── Token management ───────────────────────────────────────────────
def load_cached_token() -> dict | None:
    cache_path = os.getenv("PINGCODE_TOKEN_CACHE", TOKEN_CACHE_FILE)
    try:
        with open(cache_path, "r") as f:
            data = json.load(f)
        if data.get("expires_at", 0) > time.time() + 60:
            return data
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass
    return None


def save_cached_token(data: dict) -> None:
    cache_path = os.getenv("PINGCODE_TOKEN_CACHE", TOKEN_CACHE_FILE)
    try:
        with open(cache_path, "w") as f:
            json.dump(data, f)
    except OSError:
        pass  # best effort


def fetch_enterprise_token() -> str:
    cached = load_cached_token()
    if cached:
        return cached["access_token"]

    cid, csec = get_credentials()
    base = get_base_url()
    url = (
        f"{base}/v1/auth/token"
        f"?grant_type=client_credentials"
        f"&client_id={cid}"
        f"&client_secret={csec}"
    )

    req = Request(url, method="GET")
    req.add_header("Accept", "application/json")

    try:
        resp = urlopen(req, timeout=REQUEST_TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        die(f"HTTP {e.code} while fetching token", body=err_body)
    except URLError:
        die("Network error while fetching token")

    # Response may be flat or nested under "data"
    token = data.get("access_token", "")
    expires_in = data.get("expires_in", 7200)
    if not token and isinstance(data.get("data"), dict):
        token = data["data"].get("access_token", "")
        expires_in = data["data"].get("expires_in", 7200)

    if not token:
        die("No access_token in token response", body=data)

    cache = {
        "access_token": token,
        "expires_at": time.time() + int(expires_in),
    }
    save_cached_token(cache)
    return token


# ── HTTP helpers ────────────────────────────────────────────────────
def api_request(
    method: str,
    path: str,
    *,
    params: dict | None = None,
    body: dict | None = None,
) -> Dict[str, Any]:
    token = fetch_enterprise_token()
    base = get_base_url()
    url = f"{base}{path}"

    if params:
        # Filter out None values
        filtered = {k: v for k, v in params.items() if v is not None}
        if filtered:
            url += "?" + urlencode(filtered)

    data_bytes = None
    if body is not None:
        data_bytes = json.dumps(body).encode("utf-8")

    req = Request(url, data=data_bytes, method=method.upper())
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")

    try:
        resp = urlopen(req, timeout=REQUEST_TIMEOUT)
        resp_body = resp.read().decode("utf-8")
        status = resp.status
        headers = dict(resp.headers)
    except HTTPError as e:
        resp_body = e.read().decode("utf-8", errors="replace")
        status = e.code
        headers = dict(e.headers) if hasattr(e, "headers") else {}
        # Try to parse as JSON
        try:
            parsed = json.loads(resp_body)
        except json.JSONDecodeError:
            parsed = resp_body
        return {
            "code": status,
            "error": True,
            "data": parsed,
            "rate_limit_remaining": headers.get("X-RateLimit-Remaining"),
        }
    except URLError as e:
        die(f"Network error: {e}")

    # Parse response
    try:
        parsed = json.loads(resp_body)
    except json.JSONDecodeError:
        parsed = resp_body

    return {
        "code": status,
        "data": parsed,
        "rate_limit_remaining": headers.get("X-RateLimit-Remaining"),
    }


# ── CLI entry ───────────────────────────────────────────────────────
def main() -> None:
    if len(sys.argv) < 2:
        die(
            "Usage: python3 pingcode.py '{\"method\":\"GET\",\"path\":\"/v1/myself\"}'"
        )

    raw = sys.argv[1]
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        die("Invalid JSON payload")

    if not isinstance(payload, dict):
        die("Payload must be a JSON object")

    method = (payload.get("method") or "GET").upper()
    path = payload.get("path") or ""
    params = payload.get("params") or {}
    body = payload.get("body")

    if not path:
        die("'path' is required")

    if method not in ("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"):
        die(f"Unsupported method: {method}")

    result = api_request(method, path, params=params, body=body)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
