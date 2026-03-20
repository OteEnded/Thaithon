#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the new helper functions"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
if str(LIB_DIR) not in sys.path:
    sys.path.insert(0, str(LIB_DIR))

from ไพทอน import *

# Test list helpers
print("=== Testing List Helpers ===")
ราย = [1, 2, 3]
print(f"Initial list: {ราย}")

เพิ่ม(ราย, 4)
print(f"After เพิ่ม(4): {ราย}")

ผล = นับ(ราย, 2)
print(f"นับ(2): {ผล}")

ตำแหน่ง = หาตำแหน่ง(ราย, 3)
print(f"หาตำแหน่ง(3): {ตำแหน่ง}")

แทรก(ราย, 1, 99)
print(f"After แทรก(1, 99): {ราย}")

ลบ(ราย, 99)
print(f"After ลบ(99): {ราย}")

# Test string helpers
print("\n=== Testing String Helpers ===")
ข้อความ = "  Hello World  "
print(f"Original: '{ข้อความ}'")
print(f"ตัดช่องว่าง(): '{ตัดช่องว่าง(ข้อความ)}'")

ข้อความ2 = "apple,banana,orange"
print(f"\nOriginal: '{ข้อความ2}'")
print(f"แยกข้อความ(','): {แยกข้อความ(ข้อความ2, ',')}")

รายชื่อ = ["Hello", "World", "!"]
print(f"\nหมายการ: {รายชื่อ}")
print(f"รวมข้อความ(' '): '{รวมข้อความ(' ', รายชื่อ)}'")

# Test dictionary helpers
print("\n=== Testing Dictionary Helpers ===")
พจน = {"ชื่อ": "Alice", "อายุ": 25}
print(f"Dictionary: {พจน}")
print(f"ดึงค่า('ชื่อ'): {ดึงค่า(พจน, 'ชื่อ')}")
print(f"ดึงค่า('เมือง', 'Unknown'): {ดึงค่า(พจน, 'เมือง', 'Unknown')}")

print("\n✓ All tests completed successfully!")
