#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix the __all__ list to only include defined names"""

import os
import re

# Find the Thai file
files = os.listdir('.')
thai_file = [f for f in files if 'ไพทอน' in f and f.endswith('.py')][0]

# Read the file
with open(thai_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Execute to see what's actually defined
namespace = {}
exec(content, namespace)

# Get defined names (excluding builtins and special names)
defined = set()
for name, value in namespace.items():
    if not name.startswith('_'):
        defined.add(name)

# Build new __all__ list
all_items = sorted(list(defined))

# Generate new __all__ definition
all_def = '__all__ = [\n'
for item in all_items:
    all_def += f'    "{item}",\n'
all_def += ']'

print("Generated __all__:")
print(all_def)
print()

# Find and replaceit in content
# Find the old __all__ definition
pattern = r'__all__ = \[[\s\S]*?\]'
match = re.search(pattern, content)
if match:
    old_all = match.group(0)
    new_content = content.replace(old_all, all_def)
    
    # Write back
    with open(thai_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Updated {thai_file}")
    newline = '\n'
    print(f"  Removed: {len(old_all.split(newline))} lines")
    print(f"  Added: {len(all_def.split(newline))} lines")
    print(f"  Total items in __all__: {len(all_items)}")
else:
    print("✗ Could not find __all__ definition")
