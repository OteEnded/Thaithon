"""Thai wrapper for Python re module."""

import re


def หา(รูปแบบ, ข้อความ, *, ธง=0):
    """Search pattern anywhere in text."""
    return re.search(รูปแบบ, ข้อความ, ธง)


def เริ่มตรง(รูปแบบ, ข้อความ, *, ธง=0):
    """Match pattern at beginning of text."""
    return re.match(รูปแบบ, ข้อความ, ธง)


def ตรงทั้งหมด(รูปแบบ, ข้อความ, *, ธง=0):
    """Require full-string match."""
    return re.fullmatch(รูปแบบ, ข้อความ, ธง)


def หาทั้งหมด(รูปแบบ, ข้อความ, *, ธง=0):
    """Find all non-overlapping matches."""
    return re.findall(รูปแบบ, ข้อความ, ธง)


def แทนที่(รูปแบบ, ค่าใหม่, ข้อความ, *, จำนวน=0, ธง=0):
    """Replace matches in text."""
    return re.sub(รูปแบบ, ค่าใหม่, ข้อความ, จำนวน, ธง)


def แยก(รูปแบบ, ข้อความ, *, จำนวนสูงสุด=0, ธง=0):
    """Split text using regex pattern."""
    return re.split(รูปแบบ, ข้อความ, maxsplit=จำนวนสูงสุด, flags=ธง)


def คอมไพล์(รูปแบบ, *, ธง=0):
    """Compile regex pattern for reuse."""
    return re.compile(รูปแบบ, ธง)


def หนีอักขระ(ข้อความ):
    """Escape regex metacharacters in text."""
    return re.escape(ข้อความ)


# Common flags
ไม่สนตัวพิมพ์เล็กใหญ่ = re.IGNORECASE
หลายบรรทัด = re.MULTILINE
จุดแทนขึ้นบรรทัดใหม่ = re.DOTALL


__all__ = [
    "หา",
    "เริ่มตรง",
    "ตรงทั้งหมด",
    "หาทั้งหมด",
    "แทนที่",
    "แยก",
    "คอมไพล์",
    "หนีอักขระ",
    "ไม่สนตัวพิมพ์เล็กใหญ่",
    "หลายบรรทัด",
    "จุดแทนขึ้นบรรทัดใหม่",
]
