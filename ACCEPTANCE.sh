#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

echo "=== KAGGLE AUDIT CI GATES ==="
echo ""

# 1. COMPILE: push_kernel.py passes py_compile
echo "--- Gate 1: Python Compile ---"
python3 -m py_compile push_kernel.py
echo "PASS: push_kernel.py compiles"
echo ""

# 2. KAGGLE METADATA: kernel-metadata.json has required fields
echo "--- Gate 2: Kaggle Metadata ---"
python3 -c "
import json
with open('kernel-metadata.json') as f:
    m = json.load(f)
for r in ['id', 'title', 'code_file', 'language', 'kernel_type']:
    assert r in m, f'missing {r}'
assert m['code_file'].endswith('.ipynb'), 'code_file must be a notebook'
print('PASS: kernel-metadata.json valid')
"
echo ""

echo "=== ALL GATES PASSED ==="
