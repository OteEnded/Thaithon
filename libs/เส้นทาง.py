"""Thai wrapper for file/path operations."""

from pathlib import Path
import shutil


def มีอยู่ไหม(เส้นทาง):
    """Check whether path exists."""
    return Path(เส้นทาง).exists()


def เป็นไฟล์ไหม(เส้นทาง):
    """Check whether path is a file."""
    return Path(เส้นทาง).is_file()


def เป็นโฟลเดอร์ไหม(เส้นทาง):
    """Check whether path is a directory."""
    return Path(เส้นทาง).is_dir()


def สร้างโฟลเดอร์(เส้นทาง, *, ซ้อนชั้น=True, ถ้ามีแล้วไม่พัง=True):
    """Create directory."""
    Path(เส้นทาง).mkdir(parents=ซ้อนชั้น, exist_ok=ถ้ามีแล้วไม่พัง)


def อ่านไฟล์(เส้นทาง, *, รหัส="utf-8"):
    """Read full text from file."""
    return Path(เส้นทาง).read_text(encoding=รหัส)


def เขียนไฟล์(เส้นทาง, ข้อความ, *, รหัส="utf-8"):
    """Write full text to file, creating parent dirs if needed."""
    p = Path(เส้นทาง)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(ข้อความ, encoding=รหัส)


def ต่อท้ายไฟล์(เส้นทาง, ข้อความ, *, รหัส="utf-8"):
    """Append text to file, creating parent dirs if needed."""
    p = Path(เส้นทาง)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding=รหัส) as f:
        f.write(ข้อความ)


def ลบไฟล์(เส้นทาง, *, เงียบถ้าไม่มี=True):
    """Delete file."""
    p = Path(เส้นทาง)
    if p.exists():
        p.unlink()
    elif not เงียบถ้าไม่มี:
        raise FileNotFoundError(str(เส้นทาง))


def ลบโฟลเดอร์(เส้นทาง, *, ลบทั้งโฟลเดอร์ย่อย=False, เงียบถ้าไม่มี=True):
    """Delete directory (empty or recursive)."""
    p = Path(เส้นทาง)
    if not p.exists():
        if เงียบถ้าไม่มี:
            return
        raise FileNotFoundError(str(เส้นทาง))

    if ลบทั้งโฟลเดอร์ย่อย:
        shutil.rmtree(p)
    else:
        p.rmdir()


def รายชื่อ(เส้นทาง=".", *, ซ้อนชั้น=False, แบบ="*"):
    """List files/dirs as strings."""
    p = Path(เส้นทาง)
    ตัววน = p.rglob(แบบ) if ซ้อนชั้น else p.glob(แบบ)
    return [str(x) for x in ตัววน]


def เข้าร่วมเส้นทาง(*ส่วน):
    """Join path segments."""
    return str(Path(*ส่วน))


def ชื่อไฟล์(เส้นทาง):
    """Return filename with extension."""
    return Path(เส้นทาง).name


def นามสกุล(เส้นทาง):
    """Return file suffix including dot."""
    return Path(เส้นทาง).suffix


def โฟลเดอร์แม่(เส้นทาง):
    """Return parent directory path."""
    return str(Path(เส้นทาง).parent)


def คัดลอก(ต้นทาง, ปลายทาง):
    """Copy file."""
    p = Path(ปลายทาง)
    p.parent.mkdir(parents=True, exist_ok=True)
    return shutil.copy2(ต้นทาง, ปลายทาง)


def ย้าย(ต้นทาง, ปลายทาง):
    """Move file or directory."""
    p = Path(ปลายทาง)
    p.parent.mkdir(parents=True, exist_ok=True)
    return shutil.move(ต้นทาง, ปลายทาง)


__all__ = [
    "มีอยู่ไหม",
    "เป็นไฟล์ไหม",
    "เป็นโฟลเดอร์ไหม",
    "สร้างโฟลเดอร์",
    "อ่านไฟล์",
    "เขียนไฟล์",
    "ต่อท้ายไฟล์",
    "ลบไฟล์",
    "ลบโฟลเดอร์",
    "รายชื่อ",
    "เข้าร่วมเส้นทาง",
    "ชื่อไฟล์",
    "นามสกุล",
    "โฟลเดอร์แม่",
    "คัดลอก",
    "ย้าย",
]
