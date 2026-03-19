"""
เว็บ - Thai wrapper for Python's urllib module
A library that provides Thai-named access to HTTP and URL utilities.

Usage:
    import เว็บ
    ข้อความ = เว็บ.ดึงข้อมูล("https://example.com")
    ข้อมูล = เว็บ.ดึงJSON("https://api.example.com/data")
"""

import urllib.request
import urllib.parse
import urllib.error
import json as _json


# --- HTTP Requests ---

def ดึงข้อมูล(url, *, หัว=None, หมดเวลา=10):
    """ดึงข้อมูลจาก URL (GET) คืนข้อความ (str)"""
    req = urllib.request.Request(url, headers=หัว or {})
    with urllib.request.urlopen(req, timeout=หมดเวลา) as res:
        return res.read().decode("utf-8")


def ดึงไบต์(url, *, หัว=None, หมดเวลา=10):
    """ดึงข้อมูลจาก URL (GET) คืน bytes (เหมาะสำหรับรูปภาพ/ไฟล์ไบนารี)"""
    req = urllib.request.Request(url, headers=หัว or {})
    with urllib.request.urlopen(req, timeout=หมดเวลา) as res:
        return res.read()


def ดึงJSON(url, *, หัว=None, หมดเวลา=10):
    """ดึงข้อมูล JSON จาก URL คืน dict หรือ list"""
    ข้อความ = ดึงข้อมูล(url, หัว=หัว, หมดเวลา=หมดเวลา)
    return _json.loads(ข้อความ)


def ดึงพร้อมสถานะ(url, *, หัว=None, หมดเวลา=10):
    """ดึงข้อมูลจาก URL คืน dict ที่มี สถานะ, หัวข้อ, เนื้อหา"""
    req = urllib.request.Request(url, headers=หัว or {})
    with urllib.request.urlopen(req, timeout=หมดเวลา) as res:
        return {
            "สถานะ": res.status,
            "หัวข้อ": dict(res.headers),
            "เนื้อหา": res.read().decode("utf-8"),
        }


def ส่งข้อมูล(url, ข้อมูล, *, หัว=None, หมดเวลา=10):
    """ส่ง POST request คืนข้อความตอบกลับ
    ข้อมูล: dict (form-encoded) หรือ str/bytes"""
    if isinstance(ข้อมูล, dict):
        ข้อมูล = urllib.parse.urlencode(ข้อมูล).encode("utf-8")
    elif isinstance(ข้อมูล, str):
        ข้อมูล = ข้อมูล.encode("utf-8")
    req = urllib.request.Request(url, data=ข้อมูล, headers=หัว or {}, method="POST")
    with urllib.request.urlopen(req, timeout=หมดเวลา) as res:
        return res.read().decode("utf-8")


def ส่งJSON(url, ข้อมูล, *, หัว=None, หมดเวลา=10):
    """ส่ง POST request แบบ JSON คืน dict/list"""
    ไบต์ = _json.dumps(ข้อมูล, ensure_ascii=False).encode("utf-8")
    หัวรวม = {"Content-Type": "application/json"}
    if หัว:
        หัวรวม.update(หัว)
    req = urllib.request.Request(url, data=ไบต์, headers=หัวรวม, method="POST")
    with urllib.request.urlopen(req, timeout=หมดเวลา) as res:
        return _json.loads(res.read().decode("utf-8"))


def บันทึกไฟล์(url, เส้นทาง, *, หมดเวลา=30):
    """ดาวน์โหลดไฟล์จาก URL บันทึกลงไฟล์"""
    urllib.request.urlretrieve(url, เส้นทาง)


# --- URL Utilities ---

def เข้ารหัสURL(ข้อความ, *, ปลอดภัย=""):
    """Percent-encode ข้อความสำหรับใช้ใน URL (quote)"""
    return urllib.parse.quote(ข้อความ, safe=ปลอดภัย)


def ถอดรหัสURL(ข้อความ):
    """ถอดรหัส percent-encoded URL (unquote)"""
    return urllib.parse.unquote(ข้อความ)


def แปลงพารามิเตอร์(พารามิเตอร์):
    """แปลง dict เป็น query string เช่น a=1&b=2 (urlencode)"""
    return urllib.parse.urlencode(พารามิเตอร์)


def แยกURL(url):
    """แยกส่วนประกอบของ URL (urlparse) คืน ParseResult"""
    return urllib.parse.urlparse(url)


def รวมURL(ฐาน, ส่วนเพิ่ม):
    """รวม URL สัมพัทธ์กับ URL ฐาน (urljoin)"""
    return urllib.parse.urljoin(ฐาน, ส่วนเพิ่ม)


def เพิ่มพารามิเตอร์(url, **พารามิเตอร์):
    """เพิ่ม query parameters เข้ากับ URL"""
    ส่วน = urllib.parse.urlparse(url)
    qs = urllib.parse.parse_qs(ส่วน.query)
    qs.update({k: [str(v)] for k, v in พารามิเตอร์.items()})
    ใหม่ = ส่วน._replace(query=urllib.parse.urlencode(qs, doseq=True))
    return urllib.parse.urlunparse(ใหม่)


__all__ = [
    # Requests
    "ดึงข้อมูล",
    "ดึงไบต์",
    "ดึงJSON",
    "ดึงพร้อมสถานะ",
    "ส่งข้อมูล",
    "ส่งJSON",
    "บันทึกไฟล์",
    # URL utilities
    "เข้ารหัสURL",
    "ถอดรหัสURL",
    "แปลงพารามิเตอร์",
    "แยกURL",
    "รวมURL",
    "เพิ่มพารามิเตอร์",
]
