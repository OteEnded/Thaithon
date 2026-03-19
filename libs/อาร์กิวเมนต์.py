"""
อาร์กิวเมนต์ - Thai wrapper for Python's argparse module
A library that provides Thai-named access to command-line argument parsing.

Usage:
    import อาร์กิวเมนต์
    ตัวแยก = อาร์กิวเมนต์.สร้างตัวแยก("โปรแกรมของฉัน")
    อาร์กิวเมนต์.เพิ่มอาร์กิวเมนต์(ตัวแยก, "--ชื่อ", ช่วยเหลือ="ชื่อผู้ใช้")
    ค่า = อาร์กิวเมนต์.วิเคราะห์(ตัวแยก)
"""

import argparse


def สร้างตัวแยก(คำอธิบาย="", *, ชื่อโปรแกรม=None, **kwargs):
    """สร้าง ArgumentParser ใหม่
    คำอธิบาย: ข้อความอธิบายโปรแกรม
    ชื่อโปรแกรม: ชื่อโปรแกรม (prog)"""
    return argparse.ArgumentParser(
        description=คำอธิบาย,
        prog=ชื่อโปรแกรม,
        **kwargs,
    )


def เพิ่มอาร์กิวเมนต์(ตัวแยก, *ชื่อ, ช่วยเหลือ="", ชนิด=None,
                       ค่าเริ่มต้น=None, จำเป็น=False, **kwargs):
    """เพิ่ม argument ให้กับ parser
    ชื่อ: เช่น '--ชื่อ' หรือ 'ไฟล์'
    ชนิด: เช่น str, int, float
    ค่าเริ่มต้น: ค่า default
    จำเป็น: required=True/False (ใช้กับ optional args เท่านั้น)"""
    if ชนิด is not None:
        kwargs["type"] = ชนิด
    if ค่าเริ่มต้น is not None:
        kwargs["default"] = ค่าเริ่มต้น
    if จำเป็น:
        kwargs["required"] = จำเป็น
    return ตัวแยก.add_argument(*ชื่อ, help=ช่วยเหลือ, **kwargs)


def เพิ่มธง(ตัวแยก, *ชื่อ, ช่วยเหลือ=""):
    """เพิ่ม boolean flag (store_true) เช่น --verbose"""
    return ตัวแยก.add_argument(*ชื่อ, action="store_true", help=ช่วยเหลือ)


def เพิ่มรายการ(ตัวแยก, *ชื่อ, ช่วยเหลือ="", ชนิด=str, จำเป็น=False):
    """เพิ่ม argument ที่รับหลายค่า (nargs='+')"""
    kwargs = {"type": ชนิด, "nargs": "+", "help": ช่วยเหลือ}
    if จำเป็น:
        kwargs["required"] = True
    return ตัวแยก.add_argument(*ชื่อ, **kwargs)


def เพิ่มตัวเลือก(ตัวแยก, *ชื่อ, ตัวเลือก, ช่วยเหลือ="", ค่าเริ่มต้น=None):
    """เพิ่ม argument ที่รับแค่ค่าในรายการ (choices)"""
    kwargs = {"choices": ตัวเลือก, "help": ช่วยเหลือ}
    if ค่าเริ่มต้น is not None:
        kwargs["default"] = ค่าเริ่มต้น
    return ตัวแยก.add_argument(*ชื่อ, **kwargs)


def วิเคราะห์(ตัวแยก, อาร์กิวเมนต์=None):
    """วิเคราะห์ arguments (parse_args) คืน Namespace object
    อาร์กิวเมนต์: list ของ strings (ถ้า None จะใช้ sys.argv)"""
    return ตัวแยก.parse_args(อาร์กิวเมนต์)


def วิเคราะห์บางส่วน(ตัวแยก, อาร์กิวเมนต์=None):
    """วิเคราะห์ arguments บางส่วน คืน (Namespace, รายการที่เหลือ)"""
    return ตัวแยก.parse_known_args(อาร์กิวเมนต์)


def เป็นพจนานุกรม(namespace):
    """แปลง Namespace object เป็น dict"""
    return vars(namespace)


def สร้างกลุ่ม(ตัวแยก, ชื่อ, *, คำอธิบาย=""):
    """สร้างกลุ่ม argument (add_argument_group)"""
    return ตัวแยก.add_argument_group(ชื่อ, คำอธิบาย)


def สร้างกลุ่มเลือกหนึ่ง(ตัวแยก, *, จำเป็น=False):
    """สร้างกลุ่มที่เลือกได้แค่หนึ่งตัว (mutually exclusive group)"""
    return ตัวแยก.add_mutually_exclusive_group(required=จำเป็น)


def แสดงช่วยเหลือ(ตัวแยก):
    """แสดงข้อความช่วยเหลือและออกจากโปรแกรม"""
    ตัวแยก.print_help()


__all__ = [
    "สร้างตัวแยก",
    "เพิ่มอาร์กิวเมนต์",
    "เพิ่มธง",
    "เพิ่มรายการ",
    "เพิ่มตัวเลือก",
    "วิเคราะห์",
    "วิเคราะห์บางส่วน",
    "เป็นพจนานุกรม",
    "สร้างกลุ่ม",
    "สร้างกลุ่มเลือกหนึ่ง",
    "แสดงช่วยเหลือ",
]
