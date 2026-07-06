#!/usr/bin/env python3
"""Move all HBA work items to kanban board '需求池' entry."""
import subprocess, json

PROJECT_ID = "69c63f546e0823e7c601864f"
BOARD_ID = "69c63f546e0823e7c601866f"
ENTRY_DEMAND = "69c63f546e0823e7c6018669"  # 需求池

def fetch_all_workitems():
    items = []
    page = 0
    while True:
        body = json.dumps({
            "method": "GET",
            "path": f"/v1/pjm/work_items?project_id={PROJECT_ID}&page_index={page}&page_size=50"
        })
        r = subprocess.run(["python3", "scripts/pingcode.py", body], capture_output=True, text=True)
        data = json.loads(r.stdout)
        values = data["data"]["values"]
        items.extend(values)
        if len(items) >= data["data"]["total"]:
            break
        page += 1
    return items

def update_to_board(item_id):
    body = json.dumps({
        "method": "PATCH",
        "path": f"/v1/pjm/work_items/{item_id}",
        "body": {
            "board_id": BOARD_ID,
            "entry_id": ENTRY_DEMAND
        }
    })
    r = subprocess.run(["python3", "scripts/pingcode.py", body], capture_output=True, text=True)
    result = json.loads(r.stdout)
    return result.get("code") == 200, result

if __name__ == "__main__":
    print("Fetching all work items...")
    items = fetch_all_workitems()
    print(f"Found {len(items)} items\n")

    ok = 0
    fail = 0
    for i, item in enumerate(items, 1):
        ident = item.get("identifier", "?")
        title = item.get("title", "?")[:30]
        success, result = update_to_board(item["id"])
        if success:
            ok += 1
            print(f"  ✅ {i:2d}/{len(items)} {ident} → 需求池")
        else:
            fail += 1
            msg = result.get("data", {}).get("message", str(result)[:60])
            print(f"  ❌ {i:2d}/{len(items)} {ident} | {msg}")

    print(f"\nDone! {ok} succeeded, {fail} failed")
