#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
TMP_DIR = ROOT_DIR / "tmp"
if str(LIB_DIR) not in sys.path:
    sys.path.insert(0, str(LIB_DIR))

import เจสัน
import เรกซ์
import เส้นทาง
import ซีเอสวี


def ทดสอบเจสัน():
    ข้อมูล = {"ชื่อ": "Rat", "คะแนน": [10, 20], "พร้อม": True}
    ข้อความ = เจสัน.แปลงเป็นข้อความ(ข้อมูล)
    กลับ = เจสัน.แปลงจากข้อความ(ข้อความ)
    assert กลับ == ข้อมูล

    เจสัน.เขียนไฟล์(TMP_DIR / "json" / "data.json", ข้อมูล)
    assert เจสัน.อ่านไฟล์(TMP_DIR / "json" / "data.json") == ข้อมูล

    รายการ = [{"id": 1}, {"id": 2}]
    เจสัน.เขียนบรรทัด(TMP_DIR / "json" / "list.jsonl", รายการ)
    assert เจสัน.อ่านบรรทัด(TMP_DIR / "json" / "list.jsonl") == รายการ


def ทดสอบเรกซ์():
    ข้อความ = "Order A12, B34, C56"
    assert เรกซ์.หา(r"A\d+", ข้อความ).group(0) == "A12"
    assert เรกซ์.หาทั้งหมด(r"[A-Z]\d+", ข้อความ) == ["A12", "B34", "C56"]
    assert เรกซ์.แทนที่(r"\d+", "XX", ข้อความ) == "Order AXX, BXX, CXX"
    assert เรกซ์.แยก(r"[, ]+", "a, b c") == ["a", "b", "c"]
    assert เรกซ์.ตรงทั้งหมด(r"\d{3}", "123") is not None


def ทดสอบเส้นทาง():
    base = TMP_DIR / "path"
    เส้นทาง.สร้างโฟลเดอร์(base)

    file1 = เส้นทาง.เข้าร่วมเส้นทาง(base, "note.txt")
    เส้นทาง.เขียนไฟล์(file1, "hello")
    เส้นทาง.ต่อท้ายไฟล์(file1, " world")
    assert เส้นทาง.อ่านไฟล์(file1) == "hello world"

    assert เส้นทาง.มีอยู่ไหม(file1)
    assert เส้นทาง.เป็นไฟล์ไหม(file1)
    assert not เส้นทาง.เป็นโฟลเดอร์ไหม(file1)
    assert เส้นทาง.ชื่อไฟล์(file1) == "note.txt"
    assert เส้นทาง.นามสกุล(file1) == ".txt"

    copied = เส้นทาง.เข้าร่วมเส้นทาง(base, "copy.txt")
    moved = เส้นทาง.เข้าร่วมเส้นทาง(base, "moved.txt")
    เส้นทาง.คัดลอก(file1, copied)
    เส้นทาง.ย้าย(copied, moved)
    assert เส้นทาง.มีอยู่ไหม(moved)


def ทดสอบซีเอสวี():
    แถว = [["ชื่อ", "อายุ"], ["A", "20"], ["B", "30"]]
    ซีเอสวี.เขียนไฟล์(TMP_DIR / "csv" / "basic.csv", แถว)
    อ่านกลับ = ซีเอสวี.อ่านไฟล์(TMP_DIR / "csv" / "basic.csv")
    assert อ่านกลับ == แถว

    ซีเอสวี.ต่อท้ายไฟล์(TMP_DIR / "csv" / "basic.csv", [["C", "40"]])
    อ่านกลับ2 = ซีเอสวี.อ่านไฟล์(TMP_DIR / "csv" / "basic.csv")
    assert อ่านกลับ2[-1] == ["C", "40"]

    dict_rows = [
        {"name": "alice", "age": "21"},
        {"name": "bob", "age": "22"},
    ]
    ซีเอสวี.เขียนพจนานุกรม(TMP_DIR / "csv" / "dict.csv", dict_rows)
    read_dict = ซีเอสวี.อ่านเป็นพจนานุกรม(TMP_DIR / "csv" / "dict.csv")
    assert read_dict == dict_rows


def main():
    ทดสอบเจสัน()
    ทดสอบเรกซ์()
    ทดสอบเส้นทาง()
    ทดสอบซีเอสวี()
    print("All new libraries passed tests.")


if __name__ == "__main__":
    main()
