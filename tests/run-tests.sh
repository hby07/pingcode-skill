#!/usr/bin/env bash
# PingCode Skill Test Suite
# Validates structure, SDO compliance, bulletproofing, and script integrity
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PASS=0
FAIL=0
ERRORS=""

echo "========================================"
echo " 🔗 PingCode Skill Test Suite"
echo "========================================"
echo "Skill root: $SKILL_DIR"
echo "Test time: $(date)"
echo ""

VERBOSE=false
while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v) VERBOSE=true; shift ;;
        --help|-h)
            echo "Usage: $0 [--verbose] [--help]"
            echo "  -v, --verbose   Show detailed output"
            exit 0 ;;
        *) echo "Unknown: $1"; exit 1 ;;
    esac
done

report() {
    local name="$1" status="$2" detail="${3:-}"
    if [ "$status" = "PASS" ]; then
        PASS=$((PASS + 1))
        echo "  ✅ $name"
    else
        FAIL=$((FAIL + 1))
        echo "  ❌ $name"
        if [ -n "$detail" ]; then
            ERRORS="${ERRORS}     ${detail}"$'\n'
        fi
    fi
    if [ "$VERBOSE" = true ] && [ -n "$detail" ]; then
        echo "       $detail"
    fi
    return 0
}

check_file_exists() {
    local file="$1" label="$2"
    if [ -f "$file" ]; then
        report "$label" PASS
    else
        report "$label" FAIL "missing: $file"
    fi
}

check_dir_exists() {
    local dir="$1" label="$2"
    if [ -d "$dir" ]; then
        report "$label" PASS
    else
        report "$label" FAIL "missing: $dir"
    fi
}

check_description() {
    local file="$1" label="$2"
    if [ ! -f "$file" ]; then
        report "$label description SDO" FAIL "file not found"
        return
    fi
    local desc
    desc=$(sed -n '/^---$/,/^---$/p' "$file" | grep "^description:" | head -1)
    if echo "$desc" | grep -qi '^description:\s*"\{0,1\}Use when'; then
        report "$label description SDO" PASS
    else
        report "$label description SDO" FAIL "must start with 'Use when'"
        if [ "$VERBOSE" = true ]; then
            echo "       Found: $desc"
        fi
    fi
}

check_grep() {
    local pattern="$1" file="$2" label="$3"
    if grep -qiE "$pattern" "$file" 2>/dev/null; then
        report "$label" PASS
    else
        report "$label" FAIL "no match for: $pattern"
    fi
}

MODULES="auth org product workitem code test release plan wiki project project_config"

# 1. Module Structure
echo "─── 1. Module Structure ───"
for mod in $MODULES; do
    check_dir_exists "$SKILL_DIR/$mod" "Module $mod/"
done

# 2. File Coverage
echo "─── 2. File Coverage ───"
for f in SKILL.md README.md REFERENCE.md CONTRIBUTING.md LICENSE; do
    check_file_exists "$SKILL_DIR/$f" "Root $f"
done
for mod in $MODULES; do
    check_file_exists "$SKILL_DIR/$mod/SKILL.md" "$mod/SKILL.md"
    check_file_exists "$SKILL_DIR/$mod/APIs.md" "$mod/APIs.md"
done
check_file_exists "$SKILL_DIR/scripts/pingcode.py" "scripts/pingcode.py"
check_file_exists "$SKILL_DIR/workflow/apis.md" "workflow/apis.md"

# 3. SDO Description Compliance
echo "─── 3. SDO Description Check ───"
check_description "$SKILL_DIR/SKILL.md" "Root"
for mod in $MODULES; do
    check_description "$SKILL_DIR/$mod/SKILL.md" "$mod"
done

# 4. Bulletproofing
echo "─── 4. Bulletproofing ───"
check_grep "⚠️|必知规则|不要" "$SKILL_DIR/SKILL.md" "Root has bulletproofing"
for rule in "按需加载|不要一次性" "硬编码|hardcode" "分页|size.*最大" "PATCH|不要用 PUT" "限流|RateLimit"; do
    check_grep "$rule" "$SKILL_DIR/SKILL.md" "Bulletproof: $rule"
done

# 5. Python Script Syntax
echo "─── 5. Script Validation ───"
if python3 -c "import py_compile; py_compile.compile('$SKILL_DIR/scripts/pingcode.py', doraise=True)" 2>/dev/null; then
    report "pingcode.py syntax" PASS
else
    report "pingcode.py syntax" FAIL "Python syntax error"
fi

# 6. Module Index in Root SKILL.md
echo "─── 6. Module Index ───"
for mod in $MODULES; do
    check_grep "\`$mod\`" "$SKILL_DIR/SKILL.md" "Index: $mod"
done

# 7. Flowchart Coverage
echo "─── 7. Flowchart Coverage ───"
check_grep "digraph" "$SKILL_DIR/SKILL.md" "Root SKILL.md diagram"
check_grep "digraph" "$SKILL_DIR/workflow/apis.md" "Workflow diagram"

# 8. README Consistency
echo "─── 8. README Checks ───"
check_grep "REFERENCE.md" "$SKILL_DIR/README.md" "README → REFERENCE.md"
check_grep "Before|After|❌ Before|✅ After" "$SKILL_DIR/README.md" "README has Before/After"

# 9. Workflow Quality
echo "─── 9. Workflow Checks ───"
check_grep "常见错误|⚠️" "$SKILL_DIR/workflow/apis.md" "Workflow error table"

# Summary
echo ""
echo "========================================"
echo " Results: $PASS passed, $FAIL failed"
echo "========================================"
if [ $FAIL -gt 0 ]; then
    echo ""
    echo "Failed:"
    echo -n "$ERRORS"
    exit 1
fi
exit 0