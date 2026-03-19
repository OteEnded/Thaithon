"""
สถิติ - Thai wrapper for Python's statistics module
A library that provides Thai-named access to statistical functions.

Usage:
    import สถิติ
    ค่าเฉลี่ย = สถิติ.เฉลี่ย([1, 2, 3, 4, 5])
    ค่ากลาง = สถิติ.มัธยฐาน([1, 2, 3, 4, 5])
"""

import statistics

# Central tendency
def เฉลี่ย(ข้อมูล):
    """คำนวณค่าเฉลี่ย (mean/average)"""
    return statistics.mean(ข้อมูล)

def ค่าเฉลี่ย(ข้อมูล):
    """alias สำหรับเฉลี่ย"""
    return statistics.mean(ข้อมูล)

def มัธยฐาน(ข้อมูล):
    """คำนวณค่ามัธยฐาน (median) - ค่ากลาง"""
    return statistics.median(ข้อมูล)

def มัธยฐานต่ำ(ข้อมูล):
    """คำนวณค่ามัธยฐานต่ำ (median_low)"""
    return statistics.median_low(ข้อมูล)

def มัธยฐานสูง(ข้อมูล):
    """คำนวณค่ามัธยฐานสูง (median_high)"""
    return statistics.median_high(ข้อมูล)

def โหมด(ข้อมูล):
    """คำนวณ mode - ค่าที่ปรากฏบ่อยสุด"""
    return statistics.mode(ข้อมูล)

def โหมดหลายตัว(ข้อมูล):
    """หา mode ทั้งหมด (multimode) - รายการค่าที่ปรากฏบ่อยสุด"""
    return list(statistics.multimode(ข้อมูล))

# Dispersion
def ความแปรปรวน(ข้อมูล):
    """คำนวณความแปรปรวน variance"""
    return statistics.variance(ข้อมูล)

def ความแปรปรวนตัวอย่าง(ข้อมูล):
    """คำนวณความแปรปรวนตัวอย่าง sample variance"""
    return statistics.pvariance(ข้อมูล)

def ส่วนเบี่ยงเบน(ข้อมูล):
    """คำนวณส่วนเบี่ยงเบนมาตรฐาน (standard deviation)"""
    return statistics.stdev(ข้อมูล)

def ส่วนเบี่ยงเบนตัวอย่าง(ข้อมูล):
    """คำนวณส่วนเบี่ยงเบนมาตรฐาน ของตัวอย่าง (population stdev)"""
    return statistics.pstdev(ข้อมูล)

# Quantiles
def ควอนไทล์(ข้อมูล, จำนวนส่วน=4):
    """คำนวณควอนไทล์ (quantiles)"""
    return statistics.quantiles(ข้อมูล, n=จำนวนส่วน)

# Utility
def จำนวนสมาชิก(ข้อมูล):
    """นับจำนวนสมาชิก"""
    return len(ข้อมูล)

def รวม(ข้อมูล):
    """รวมค่า"""
    return sum(ข้อมูล)

def น้อยสุด(ข้อมูล):
    """หาค่าน้อยสุด"""
    return min(ข้อมูล)

def มากสุด(ข้อมูล):
    """หาค่ามากสุด"""
    return max(ข้อมูล)

def พิสัย(ข้อมูล):
    """คำนวณพิสัย (range) = max - min"""
    return max(ข้อมูล) - min(ข้อมูล)

def สรุป(ข้อมูล):
    """สรุปข้อมูลทางสถิติ"""
    return {
        "จำนวน": len(ข้อมูล),
        "เฉลี่ย": เฉลี่ย(ข้อมูล),
        "มัธยฐาน": มัธยฐาน(ข้อมูล),
        "ส่วนเบี่ยงเบน": ส่วนเบี่ยงเบน(ข้อมูล),
        "ความแปรปรวน": ความแปรปรวน(ข้อมูล),
        "พิสัย": พิสัย(ข้อมูล),
        "น้อยสุด": น้อยสุด(ข้อมูล),
        "มากสุด": มากสุด(ข้อมูล),
    }

# Compatibility aliases
ค่ากลาง = มัธยฐาน
มัธยมฐาน = มัธยฐาน

__all__ = [
    # Central tendency
    "เฉลี่ย",
    "ค่าเฉลี่ย",
    "มัธยฐาน",
    "ค่ากลาง",
    "มัธยฐานต่ำ",
    "มัธยฐานสูง",
    "โหมด",
    "โหมดหลายตัว",
    # Dispersion
    "ความแปรปรวน",
    "ความแปรปรวนตัวอย่าง",
    "ส่วนเบี่ยงเบน",
    "ส่วนเบี่ยงเบนตัวอย่าง",
    # Quantiles
    "ควอนไทล์",
    # Utility
    "จำนวนสมาชิก",
    "รวม",
    "น้อยสุด",
    "มากสุด",
    "พิสัย",
    "สรุป",
]
