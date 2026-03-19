"""
ระบบ - Thai wrapper for Python's os, sys, and subprocess modules
A library that provides Thai-named access to system and environment operations.

Usage:
    import ระบบ
    โฟลเดอร์ = ระบบ.โฟลเดอร์ปัจจุบัน()
    ค่า = ระบบ.ดึงตัวแปรสภาพแวดล้อม("PATH")
"""

import os
import sys
import subprocess


# Current directory
def โฟลเดอร์ปัจจุบัน():
    """ดึง working directory ปัจจุบัน (getcwd)"""
    return os.getcwd()


def เปลี่ยนโฟลเดอร์(เส้นทาง):
    """เปลี่ยน working directory (chdir)"""
    os.chdir(เส้นทาง)


# Environment variables
def ดึงตัวแปรสภาพแวดล้อม(ชื่อ, ค่าเริ่มต้น=None):
    """ดึงค่า environment variable (getenv)"""
    return os.environ.get(ชื่อ, ค่าเริ่มต้น)


def ตั้งตัวแปรสภาพแวดล้อม(ชื่อ, ค่า):
    """ตั้งค่า environment variable"""
    os.environ[ชื่อ] = str(ค่า)


def ลบตัวแปรสภาพแวดล้อม(ชื่อ):
    """ลบ environment variable"""
    os.environ.pop(ชื่อ, None)


def ตัวแปรสภาพแวดล้อมทั้งหมด():
    """ดึง environment variables ทั้งหมดเป็น dict"""
    return dict(os.environ)


# Path separator
ตัวแบ่งเส้นทาง = os.sep
ตัวแบ่งรายการเส้นทาง = os.pathsep


# System info
def ระบบปฏิบัติการ():
    """ดึงชื่อระบบปฏิบัติการ (os.name: 'nt' = Windows, 'posix' = Unix)"""
    return os.name


def รันบน():
    """ดึงชื่อ platform (sys.platform)"""
    return sys.platform


def เวอร์ชันPython():
    """ดึงเวอร์ชัน Python"""
    return sys.version


def เวอร์ชันPythonสั้น():
    """ดึงเวอร์ชัน Python แบบสั้น (tuple)"""
    return sys.version_info[:3]


# Process
def รหัสกระบวนการ():
    """ดึง process ID (PID)"""
    return os.getpid()


def รันคำสั่ง(คำสั่ง):
    """รันคำสั่ง shell (os.system) คืนค่า exit code"""
    return os.system(คำสั่ง)


# Path utilities (wrapping os.path)
def รวมเส้นทาง(*ส่วน):
    """รวมเส้นทาง (os.path.join)"""
    return os.path.join(*ส่วน)


def เส้นทางสมบูรณ์(เส้นทาง):
    """แปลงเป็น absolute path (os.path.abspath)"""
    return os.path.abspath(เส้นทาง)


def มีอยู่ไหม(เส้นทาง):
    """ตรวจสอบว่า path มีอยู่ไหม (os.path.exists)"""
    return os.path.exists(เส้นทาง)


def ชื่อไฟล์(เส้นทาง):
    """ดึงชื่อไฟล์จาก path (os.path.basename)"""
    return os.path.basename(เส้นทาง)


def โฟลเดอร์แม่(เส้นทาง):
    """ดึง directory ของ path (os.path.dirname)"""
    return os.path.dirname(เส้นทาง)


# sys.argv
def อาร์กิวเมนต์():
    """ดึง command-line arguments (sys.argv)"""
    return sys.argv


def ออก(รหัส=0):
    """ออกจากโปรแกรม (sys.exit)"""
    sys.exit(รหัส)


# Subprocess (process management)
def รันกระบวนการ(คำสั่ง, *, จับผลลัพธ์=False, รหัส_encoding="utf-8", shell=False):
    """รันกระบวนการ (subprocess.run) คืน CompletedProcess
    ถ้า จับผลลัพธ์=True จะคืนข้อความ stdout แทน"""
    ผล = subprocess.run(
        คำสั่ง,
        capture_output=จับผลลัพธ์,
        text=True,
        encoding=รหัส_encoding,
        shell=shell,
    )
    if จับผลลัพธ์:
        return ผล.stdout
    return ผล


def รันและได้ผล(คำสั่ง, *, รหัส_encoding="utf-8", shell=False):
    """รันกระบวนการและคืน stdout เป็นข้อความ (subprocess.check_output)"""
    return subprocess.check_output(
        คำสั่ง,
        text=True,
        encoding=รหัส_encoding,
        shell=shell,
        stderr=subprocess.DEVNULL,
    ).strip()


def รันแบบเรียลไทม์(คำสั่ง, *, shell=False):
    """รันกระบวนการแบบ interactive (stdout แสดงสด) คืน exit code"""
    ผล = subprocess.run(คำสั่ง, shell=shell)
    return ผล.returncode


__all__ = [
    "โฟลเดอร์ปัจจุบัน",
    "เปลี่ยนโฟลเดอร์",
    "ดึงตัวแปรสภาพแวดล้อม",
    "ตั้งตัวแปรสภาพแวดล้อม",
    "ลบตัวแปรสภาพแวดล้อม",
    "ตัวแปรสภาพแวดล้อมทั้งหมด",
    "ตัวแบ่งเส้นทาง",
    "ตัวแบ่งรายการเส้นทาง",
    "ระบบปฏิบัติการ",
    "รันบน",
    "เวอร์ชันPython",
    "เวอร์ชันPythonสั้น",
    "รหัสกระบวนการ",
    "รันคำสั่ง",
    "รวมเส้นทาง",
    "เส้นทางสมบูรณ์",
    "มีอยู่ไหม",
    "ชื่อไฟล์",
    "โฟลเดอร์แม่",
    "อาร์กิวเมนต์",
    "ออก",
    # Subprocess
    "รันกระบวนการ",
    "รันและได้ผล",
    "รันแบบเรียลไทม์",
]
