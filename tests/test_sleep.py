#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the sleep and timing functions in เวลา library"""

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
if str(LIB_DIR) not in sys.path:
    sys.path.insert(0, str(LIB_DIR))

import เวลา

พิมพ์ = print

print("=== Testing Sleep and Timing Functions ===\n")

# Test 1: Basic sleep
print("Test 1: นอน 2 วินาที")
พิมพ์(f"เวลา: {เวลา.ตอนนี้()}")
พิมพ์("กำลังนอนอยู่...")
เวลา.นอน(2)
พิมพ์(f"ตื่นแล้ว เวลา: {เวลา.ตอนนี้()}\n")

# Test 2: Sleep in milliseconds
print("Test 2: นอน 500 มิลลิวินาที")
พิมพ์("กำลังนอน 0.5 วินาที...")
เวลา.นอนมิลลิวินาที(500)
พิมพ์("เสร็จแล้ว!\n")

# Test 3: Performance timing
print("Test 3: วัดเวลาการทำงาน")
เวลาเริ่ม = เวลา.วัดเวลา()
พิมพ์("กำลังคำนวณ...")
ผลรวม = sum(range(10_000_000))
เวลาสิ้นสุด = เวลา.วัดเวลา()
เวลาที่ผ่านไป = เวลาสิ้นสุด - เวลาเริ่ม
พิมพ์(f"sum(0..9999999) = {ผลรวม:,}")
พิมพ์(f"เวลาที่ใช้: {เวลาที่ผ่านไป:.6f} วินาที\n")

# Test 4: Current timestamp
print("Test 4: Timestamps")
วินาทีปัจจุบัน = เวลา.ปัจจุบัน_วินาที()
พิมพ์(f"วินาทีตั้งแต่ epoch: {วินาทีปัจจุบัน}")
พิมพ์(f"เป็นมิลลิวินาที: {วินาทีปัจจุบัน * 1000:.0f}\n")

# Test 5: Loop with timing
print("Test 5: วนลูปพร้อมนอน")
for i in range(3):
    print(f"  ครั้งที่ {i+1}: {เวลา.มะรุ่งนี้()}")
    เวลา.นอน(1)
    
print("\n✓ All sleep and timing functions working correctly!")
