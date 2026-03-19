"""
คณิต - Thai wrapper for Python's math module
A library that provides Thai-named access to common math functions.

Usage:
    import คณิต
    ผล = คณิต.ปัดขึ้น(3.2)
    
Or:
    from คณิต import ปัดขึ้น, รากที่สอง, ปัดลง
    ผล = ปัดขึ้น(3.2)
"""

import math

# Constants
พาย = math.pi
ออยเลอร์ = math.e

# Rounding functions
def ปัดขึ้น(เลข):
    """ปัดตัวเลขขึ้น (ceil)"""
    return math.ceil(เลข)

def ปัดลง(เลข):
    """ปัดตัวเลขลง (floor)"""
    return math.floor(เลข)

def ปัดเศษ(เลข, ตำแหน่ง=0):
    """ปัดเศษตัวเลข (round)"""
    return round(เลข, ตำแหน่ง)

# Power and root functions
def รากที่สอง(เลข):
    """หารากที่สอง (sqrt)"""
    return math.sqrt(เลข)

def ยกกำลัง(เลข, กำลัง):
    """ยกตัวเลขขึ้นกำลัง (pow)"""
    return math.pow(เลข, กำลัง)

def เอก็ซโปเนนเชียล(เลข):
    """คำนวณ e ยกกำลัง เลข (exp)"""
    return math.exp(เลข)

# Logarithmic functions
def ลอการิทึม(เลข, ฐาน=math.e):
    """คำนวณลอการิทึม (log)"""
    return math.log(เลข, ฐาน)

def ลอการิทึมฐานสิบ(เลข):
    """คำนวณลอการิทึมฐาน 10 (log10)"""
    return math.log10(เลข)

def ลอการิทึมฐานสอง(เลข):
    """คำนวณลอการิทึมฐาน 2 (log2)"""
    return math.log2(เลข)

# Trigonometric functions
def ไซน์(เรเดียน):
    """คำนวณ sin (sine)"""
    return math.sin(เรเดียน)

def โคซาย(เรเดียน):
    """คำนวณ cos (cosine)"""
    return math.cos(เรเดียน)

def แทนเจนต์(เรเดียน):
    """คำนวณ tan (tangent)"""
    return math.tan(เรเดียน)

def ไซน์ผกผัน(เลข):
    """คำนวณ asin (arcsine)"""
    return math.asin(เลข)

def โคซายผกผัน(เลข):
    """คำนวณ acos (arccosine)"""
    return math.acos(เลข)

def แทนเจนต์ผกผัน(เลข):
    """คำนวณ atan (arctangent)"""
    return math.atan(เลข)

# Angle conversion
def องศาเป็นเรเดียน(องศา):
    """แปลงองศาเป็นเรเดียน (radians)"""
    return math.radians(องศา)

def เรเดียนเป็นองศา(เรเดียน):
    """แปลงเรเดียนเป็นองศา (degrees)"""
    return math.degrees(เรเดียน)

# Absolute and comparison
def ค่าสัมบูรณ์(เลข):
    """หาค่าสัมบูรณ์ (fabs)"""
    return math.fabs(เลข)

def มากสุด(*เลขทั้งหมด):
    """หาค่ามากสุด (max)"""
    return max(เลขทั้งหมด)

def น้อยสุด(*เลขทั้งหมด):
    """หาค่าน้อยสุด (min)"""
    return min(เลขทั้งหมด)

def รวม(*เลขทั้งหมด):
    """รวมตัวเลข (sum)"""
    return sum(เลขทั้งหมด)

# Other useful functions
def แฟกทอเรียล(เลข):
    """คำนวณแฟกทอเรียล (factorial)"""
    return math.factorial(int(เลข))

def จำนวนเต็ม(เลข):
    """ตัดเศษทศนิยมทิ้ง (trunc)"""
    return math.trunc(เลข)

# GCD and LCM
def หารลงตัวสูงสุด(ก, ข):
    """หาตัวหารรวมสูงสุด GCD (greatest common divisor)"""
    return math.gcd(ก, ข)

def คูณรวมต่ำสุด(ก, ข):
    """หาตัวคูณรวมต่ำสุด LCM (least common multiple)"""
    return math.lcm(ก, ข)

# Distance
def ระยะห่าง(x, y):
    """คำนวณระยะห่าง (hypotenuse) โดยใช้ hypot"""
    return math.hypot(x, y)

def ระยะห่าง3มิติ(x, y, z):
    """คำนวณระยะห่างในพื้นที่ 3 มิติ"""
    return math.sqrt(x**2 + y**2 + z**2)

# Advanced angle functions
def แทนเจนต์ผกผัน2(y, x):
    """คำนวณ atan2 - arctangent ของ y/x โดยคำนึงถึงจตุภาค"""
    return math.atan2(y, x)

# Type checking
def เป็นตัวเลขบ้าง(เลข):
    """ตรวจสอบว่าเป็น NaN (Not a Number) หรือไม่"""
    return math.isnan(เลข)

def เป็นอนันต์บ้าง(เลข):
    """ตรวจสอบว่าเป็น infinity หรือไม่"""
    return math.isinf(เลข)

def เป็นตัวเลขจริงบ้าง(เลข):
    """ตรวจสอบว่าเป็นตัวเลขจริง (ไม่ใช่ NaN หรือ infinity) หรือไม่"""
    return math.isfinite(เลข)

# Modulo and remainder
def หารเอาเศษ(เลขตั้ง, เลขหาร):
    """หารเอาเศษ (modulo) - เหมือน % operator"""
    return math.fmod(เลขตั้ง, เลขหาร)

# Combinatorics
def จัดหมู่(n, k):
    """คำนวณจัดหมู่ nCk (combination)"""
    return math.comb(n, k)

def จัดลำดับ(n, k):
    """คำนวณจัดลำดับ nPk (permutation)"""
    return math.perm(n, k)

# Sign operations
def คัดลอกเครื่องหมาย(เลข, เครื่องหมายมาจาก):
    """คัดลอกเครื่องหมายจากตัวเลขหนึ่งไปยังอีกตัวหนึ่ง (copysign)"""
    return math.copysign(เลข, เครื่องหมายมาจาก)

# Sum with better precision
def รวมแม่นยำ(*เลขทั้งหมด):
    """รวมตัวเลขพร้อมความแม่นยำสูงกว่า (fsum)"""
    return math.fsum(เลขทั้งหมด)

# Compatibility aliases
ปัด = ปัดเศษ
สแควร์รูท = รากที่สอง
กำลัง = ยกกำลัง
ไทย_เลือก = จัดหมู่
ไทย_เรียง = จัดลำดับ

__all__ = [
    # Constants
    "พาย",
    "ออยเลอร์",
    # Rounding
    "ปัดขึ้น",
    "ปัดลง",
    "ปัดเศษ",
    "ปัด",
    "จำนวนเต็ม",
    # Power and root
    "รากที่สอง",
    "สแควร์รูท",
    "ยกกำลัง",
    "กำลัง",
    "เอก็ซโปเนนเชียล",
    # Logarithmic
    "ลอการิทึม",
    "ลอการิทึมฐานสิบ",
    "ลอการิทึมฐานสอง",
    # Trigonometric
    "ไซน์",
    "โคซาย",
    "แทนเจนต์",
    "ไซน์ผกผัน",
    "โคซายผกผัน",
    "แทนเจนต์ผกผัน",
    "แทนเจนต์ผกผัน2",
    # Angle conversion
    "องศาเป็นเรเดียน",
    "เรเดียนเป็นองศา",
    # Absolute and comparison
    "ค่าสัมบูรณ์",
    "มากสุด",
    "น้อยสุด",
    "รวม",
    "รวมแม่นยำ",
    # GCD and LCM
    "หารลงตัวสูงสุด",
    "คูณรวมต่ำสุด",
    # Distance
    "ระยะห่าง",
    "ระยะห่าง3มิติ",
    # Type checking
    "เป็นตัวเลขบ้าง",
    "เป็นอนันต์บ้าง",
    "เป็นตัวเลขจริงบ้าง",
    # Modulo
    "หารเอาเศษ",
    # Combinatorics
    "จัดหมู่",
    "จัดลำดับ",
    "ไทย_เลือก",
    "ไทย_เรียง",
    # Sign
    "คัดลอกเครื่องหมาย",
    # Other
    "แฟกทอเรียล",
]
