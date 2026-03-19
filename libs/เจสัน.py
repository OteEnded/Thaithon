"""Thai wrapper for Python json module."""

import json
from pathlib import Path


def แปลงเป็นข้อความ(ข้อมูล, *, ย่อหน้า=2, ascii_only=False, เรียงคีย์=False):
    """Serialize Python object to JSON text."""
    return json.dumps(ข้อมูล, ensure_ascii=ascii_only, indent=ย่อหน้า, sort_keys=เรียงคีย์)


def แปลงจากข้อความ(ข้อความ):
    """Parse JSON text to Python object."""
    return json.loads(ข้อความ)


def เขียนไฟล์(เส้นทางไฟล์, ข้อมูล, *, ย่อหน้า=2, ascii_only=False, เรียงคีย์=False, รหัส="utf-8"):
    """Write Python object to JSON file."""
    Path(เส้นทางไฟล์).parent.mkdir(parents=True, exist_ok=True)
    with open(เส้นทางไฟล์, "w", encoding=รหัส) as f:
        json.dump(ข้อมูล, f, ensure_ascii=ascii_only, indent=ย่อหน้า, sort_keys=เรียงคีย์)


def อ่านไฟล์(เส้นทางไฟล์, *, รหัส="utf-8"):
    """Read JSON file to Python object."""
    with open(เส้นทางไฟล์, "r", encoding=รหัส) as f:
        return json.load(f)


def เขียนบรรทัด(เส้นทางไฟล์, รายการข้อมูล, *, รหัส="utf-8"):
    """Write JSON Lines (.jsonl), one object per line."""
    Path(เส้นทางไฟล์).parent.mkdir(parents=True, exist_ok=True)
    with open(เส้นทางไฟล์, "w", encoding=รหัส) as f:
        for รายการ in รายการข้อมูล:
            f.write(json.dumps(รายการ, ensure_ascii=False))
            f.write("\n")


def อ่านบรรทัด(เส้นทางไฟล์, *, รหัส="utf-8"):
    """Read JSON Lines (.jsonl), returns list of objects."""
    ผลลัพธ์ = []
    with open(เส้นทางไฟล์, "r", encoding=รหัส) as f:
        for บรรทัด in f:
            บรรทัด = บรรทัด.strip()
            if บรรทัด:
                ผลลัพธ์.append(json.loads(บรรทัด))
    return ผลลัพธ์


# Compatibility aliases
dumps = แปลงเป็นข้อความ
loads = แปลงจากข้อความ
dump_file = เขียนไฟล์
load_file = อ่านไฟล์


__all__ = [
    "แปลงเป็นข้อความ",
    "แปลงจากข้อความ",
    "เขียนไฟล์",
    "อ่านไฟล์",
    "เขียนบรรทัด",
    "อ่านบรรทัด",
    "dumps",
    "loads",
    "dump_file",
    "load_file",
]
