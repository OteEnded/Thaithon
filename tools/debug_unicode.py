#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug the Unicode issue with the module"""

import sys
import os

# Get the Thai filename
files = os.listdir('.')
thai_file = [f for f in files if 'ไพท่อน' in f and f.endswith('.py')][0]

print(f"Loading file: {thai_file}")
print(f"File repr: {repr(thai_file)}")

# Load the file and check what gets defined
namespace = {}
with open(thai_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for จำนวนจริง in the file
if 'จำนวนจริง' in content:
    print("✓ Found 'จำนวนจริง' in file")
    # Find all occurrences
    lines = content.split('\n')
    for i, line in enumerate(lines[:50], 1):
        if 'จำนวนจริง' in line:
            print(f"  Line {i}: {repr(line)}")

# Execute the module
try:
    exec(content, namespace)
    print("\n✓ Module loaded successfully")
except Exception as e:
    print(f"\n✗ Error loading module: {e}")
    import traceback
    traceback.print_exc()

# Check what's defined
print("\n=== Checking what's defined ===")
test_names = ['จำนวนจริง', 'จำนวนเต็ม', 'จํานวนจริง', 'จํานวนเต็ม']
for name in test_names:
    if name in namespace:
        print(f"✓ {repr(name)} is defined")
    else:
        print(f"✗ {repr(name)} is NOT defined")

# Check __all__
if '__all__' in namespace:
    all_list = namespace['__all__']
    print(f"\n=== __all__ contains {len(all_list)} items ===")
    
    # Check which ones are missing
    missing = []
    for item in all_list:
        if item not in namespace:
            missing.append(item)
    
    if missing:
        print(f"\n✗ Missing items in __all__: {len(missing)}")
        for item in missing[:10]:
            print(f"  - {repr(item)}")
    else:
        print("✓ All items in __all__ are defined")
