"""Thai wrapper for Python csv module."""

import csv
from pathlib import Path


def อ่านไฟล์(เส้นทางไฟล์, *, ตัวคั่น=",", รหัส="utf-8"):
    """Read CSV rows as list of lists."""
    with open(เส้นทางไฟล์, "r", newline="", encoding=รหัส) as f:
        reader = csv.reader(f, delimiter=ตัวคั่น)
        return [แถว for แถว in reader]


def อ่านเป็นพจนานุกรม(เส้นทางไฟล์, *, ตัวคั่น=",", รหัส="utf-8"):
    """Read CSV rows as list of dictionaries."""
    with open(เส้นทางไฟล์, "r", newline="", encoding=รหัส) as f:
        reader = csv.DictReader(f, delimiter=ตัวคั่น)
        return [dict(แถว) for แถว in reader]


def เขียนไฟล์(เส้นทางไฟล์, แถวข้อมูล, *, ตัวคั่น=",", รหัส="utf-8"):
    """Write CSV rows from list of lists."""
    Path(เส้นทางไฟล์).parent.mkdir(parents=True, exist_ok=True)
    with open(เส้นทางไฟล์, "w", newline="", encoding=รหัส) as f:
        writer = csv.writer(f, delimiter=ตัวคั่น)
        writer.writerows(แถวข้อมูล)


def ต่อท้ายไฟล์(เส้นทางไฟล์, แถวข้อมูล, *, ตัวคั่น=",", รหัส="utf-8"):
    """Append CSV rows from list of lists."""
    Path(เส้นทางไฟล์).parent.mkdir(parents=True, exist_ok=True)
    with open(เส้นทางไฟล์, "a", newline="", encoding=รหัส) as f:
        writer = csv.writer(f, delimiter=ตัวคั่น)
        writer.writerows(แถวข้อมูล)


def เขียนพจนานุกรม(เส้นทางไฟล์, แถวข้อมูล, *, คีย์=None, ตัวคั่น=",", รหัส="utf-8"):
    """Write CSV rows from list of dictionaries."""
    if not แถวข้อมูล and คีย์ is None:
        raise ValueError("ต้องระบุข้อมูลหรือคีย์อย่างน้อยหนึ่งอย่าง")

    ฟิลด์ = คีย์ or list(แถวข้อมูล[0].keys())

    Path(เส้นทางไฟล์).parent.mkdir(parents=True, exist_ok=True)
    with open(เส้นทางไฟล์, "w", newline="", encoding=รหัส) as f:
        writer = csv.DictWriter(f, fieldnames=ฟิลด์, delimiter=ตัวคั่น)
        writer.writeheader()
        writer.writerows(แถวข้อมูล)


__all__ = [
    "อ่านไฟล์",
    "อ่านเป็นพจนานุกรม",
    "เขียนไฟล์",
    "ต่อท้ายไฟล์",
    "เขียนพจนานุกรม",
]
