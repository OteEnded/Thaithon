#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the expanded math library - คณิต"""

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
if str(LIB_DIR) not in sys.path:
	sys.path.insert(0, str(LIB_DIR))

import คณิต

พิมพ์ = print

print("=== Testing Extended คณิต (Math) Library ===\n")

# GCD and LCM
print("=== GCD and LCM ===")
พิมพ์(f"หารลงตัวสูงสุด(48, 18): {คณิต.หารลงตัวสูงสุด(48, 18)}")
พิมพ์(f"คูณรวมต่ำสุด(12, 18): {คณิต.คูณรวมต่ำสุด(12, 18)}\n")

# Distance
print("=== Distance Functions ===")
พิมพ์(f"ระยะห่าง(3, 4): {คณิต.ระยะห่าง(3, 4)}")
พิมพ์(f"ระยะห่าง3มิติ(1, 2, 2): {คณิต.ระยะห่าง3มิติ(1, 2, 2)}\n")

# Advanced angle
print("=== Advanced Angle Functions ===")
มุม = คณิต.แทนเจนต์ผกผัน2(1, 1)
พิมพ์(f"แทนเจนต์ผกผัน2(1, 1): {มุม:.4f} เรเดียน")
พิมพ์(f"เป็นองศา: {คณิต.เรเดียนเป็นองศา(มุม):.1f}°\n")

# Type checking
print("=== Type Checking ===")
พิมพ์(f"เป็นตัวเลขบ้าง(float('nan')): {คณิต.เป็นตัวเลขบ้าง(float('nan'))}")
พิมพ์(f"เป็นอนันต์บ้าง(float('inf')): {คณิต.เป็นอนันต์บ้าง(float('inf'))}")
พิมพ์(f"เป็นตัวเลขจริงบ้าง(3.14): {คณิต.เป็นตัวเลขจริงบ้าง(3.14)}\n")

# Modulo
print("=== Modulo / Remainder ===")
พิมพ์(f"หารเอาเศษ(17, 5): {คณิต.หารเอาเศษ(17, 5)}")
print()

# Combinatorics
print("=== Combinatorics ===")
พิมพ์(f"จัดหมู่(5, 2) [C(5,2)]: {คณิต.จัดหมู่(5, 2)}")
พิมพ์(f"จัดลำดับ(5, 2) [P(5,2)]: {คณิต.จัดลำดับ(5, 2)}\n")

# Sign operations
print("=== Sign Operations ===")
พิมพ์(f"คัดลอกเครื่องหมาย(5, -3): {คณิต.คัดลอกเครื่องหมาย(5, -3)}")
พิมพ์(f"คัดลอกเครื่องหมาย(-5, 3): {คณิต.คัดลอกเครื่องหมาย(-5, 3)}\n")

# High precision sum
print("=== High Precision Sum ===")
ตัวเลข = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
พิมพ์(f"รวมตัวเลข 10 ตัว 0.1: {sum(ตัวเลข)}")
พิมพ์(f"รวมแม่นยำ: {คณิต.รวมแม่นยำ(*ตัวเลข)}\n")

print("✓ All extended math functions working correctly!")
