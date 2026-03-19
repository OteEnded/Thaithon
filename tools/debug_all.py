#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check what's in __all__"""

import sys
import os

# Get the Thai filename
files = os.listdir('.')
thai_file = [f for f in files if 'ไพท่อน' in f and f.endswith('.py')][0]

# Load module
namespace = {}
with open(thai_file, 'r', encoding='utf-8') as f:
    content = f.read()

exec(content, namespace)

# Check __all__
all_list = namespace['__all__']

# Look for the problematic names
print("=== Items in __all__ related to จำนวน ===")
for item in all_list:
    if 'จ' in item and ('นวน' in item or 'ำนวน' in item or 'ํานวน' in item):
        print(f"  {repr(item)}: defined={item in namespace}")

print("\n=== Items in __all__ related to ลำ ===")        
for item in all_list:
    if 'ลำ' in item or 'ลํา' in item or 'เรียง' in item:
        print(f"  {repr(item)}: defined={item in namespace}")

print("\n=== Items in __all__ with ต่ำ ===")
for item in all_list:
    if 'ต่ำ' in item or 'ต่ํา' in item:
        print(f"  {repr(item)}: defined={item in namespace}")
