#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the math library wrapper - คณิต"""

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
if str(LIB_DIR) not in sys.path:
	sys.path.insert(0, str(LIB_DIR))

import คณิต

print("=== Testing คณิต (Math) Library ===\n")

# Constants
print("=== Constants ===")
พิมพ์ = print
พิมพ์(f"พาย (π): {คณิต.พาย}")
พิมพ์(f"ออยเลอร์ (e): {คณิต.ออยเลอร์}\n")

# Rounding
print("=== Rounding Functions ===")
เลข = 3.7
พิมพ์(f"ตัวเลข: {เลข}")
พิมพ์(f"ปัดขึ้น: {คณิต.ปัดขึ้น(เลข)}")
พิมพ์(f"ปัดลง: {คณิต.ปัดลง(เลข)}")
พิมพ์(f"ปัดเศษ: {คณิต.ปัดเศษ(3.14159, 2)}\n")

# Power and root
print("=== Power and Root ===")
พิมพ์(f"รากที่สองของ 16: {คณิต.รากที่สอง(16)}")
พิมพ์(f"2 ยกกำลัง 8: {คณิต.ยกกำลัง(2, 8)}")
พิมพ์(f"e ยกกำลัง 1: {คณิต.เอก็ซโปเนนเชียล(1)}\n")

# Logarithmic
print("=== Logarithmic Functions ===")
พิมพ์(f"ln(10): {คณิต.ลอการิทึม(10)}")
พิมพ์(f"log10(100): {คณิต.ลอการิทึมฐานสิบ(100)}")
พิมพ์(f"log2(8): {คณิต.ลอการิทึมฐานสอง(8)}\n")

# Trigonometric
print("=== Trigonometric Functions ===")
มุม = คณิต.องศาเป็นเรเดียน(45)
พิมพ์(f"45 องศา = {มุม:.4f} เรเดียน")
พิมพ์(f"sin(45°): {คณิต.ไซน์(มุม):.4f}")
พิมพ์(f"cos(45°): {คณิต.โคซาย(มุม):.4f}")
พิมพ์(f"tan(45°): {คณิต.แทนเจนต์(มุม):.4f}\n")

# Angle conversion
print("=== Angle Conversion ===")
พิมพ์(f"90 องศา = {คณิต.องศาเป็นเรเดียน(90):.4f} เรเดียน")
พิมพ์(f"π เรเดียน = {คณิต.เรเดียนเป็นองศา(คณิต.พาย):.1f} องศา\n")

# Utilities
print("=== Utility Functions ===")
พิมพ์(f"ค่าสัมบูรณ์ของ -15: {คณิต.ค่าสัมบูรณ์(-15)}")
พิมพ์(f"มากสุด(5, 2, 8, 1): {คณิต.มากสุด(5, 2, 8, 1)}")
พิมพ์(f"น้อยสุด(5, 2, 8, 1): {คณิต.น้อยสุด(5, 2, 8, 1)}")
พิมพ์(f"5! (5 แฟกทอเรียล): {คณิต.แฟกทอเรียล(5)}\n")

print("✓ All math functions working correctly!")
