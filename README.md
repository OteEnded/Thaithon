# Thaithon

<p align="center">
  <img src="https://raw.githubusercontent.com/OteEnded/Thaithon/main/logo.png" alt="Thaithon logo" width="200"/>
</p>

โปรเจกต์นี้เป็น playground สำหรับทำ helper/library ภาษาไทยบน Python โดยตั้งชื่อฟังก์ชันให้เป็นคำไทยที่อ่านง่าย และใช้งานได้ใกล้เคียง library มาตรฐาน

## Write Python in Thai 🇹🇭

Thaithon is an experimental layer that lets you write Python code using Thai-style syntax.

## Install

```bash
pip install thaithon
```

## Example

```python
from thaithon import พิมพ์

พิมพ์("สวัสดีโลก")
```

## What is this?

Thaithon is designed for:

- Learning Python in a more familiar language
- Experimenting with alternative syntax
- Having fun with code

## What this is NOT

- Not a replacement for Python
- Not intended for production use

## Why?

Because programming should be expressive - and language shouldn't be a barrier.

## Status

Experimental 🚧

## โครงสร้างโปรเจกต์

- `libs/`
  - รวม library หลักทั้งหมด
  - `ไพท่อน.py`, `ไพท่อน_builtins.py`
  - `คณิต.py`, `เวลา.py`, `สุ่ม.py`, `สถิติ.py`
  - `เจสัน.py`, `เรกซ์.py`, `เส้นทาง.py`, `ซีเอสวี.py`
- `examples/`
  - ตัวอย่างใช้งานสั้น ๆ
  - `x.py`, `y.py`
- `tests/`
  - สคริปต์ทดสอบแต่ละโมดูล
- `tools/`
  - utility/debug scripts
- `docs/`
  - บันทึก handoff หรือเอกสารประกอบ

## หมวด library ที่มีแล้ว

- Built-ins ภาษาไทย (`ไพท่อน.py`)
- Math (`คณิต.py`)
- DateTime + sleep (`เวลา.py`)
- Random (`สุ่ม.py`)
- Statistics (`สถิติ.py`)
- JSON (`เจสัน.py`)
- Regex (`เรกซ์.py`)
- File/Path (`เส้นทาง.py`)
- CSV (`ซีเอสวี.py`)
- System/OS (`ระบบ.py`)
- Web/HTTP (`เว็บ.py`)
- Argument parsing (`อาร์กิวเมนต์.py`)

## หมายเหตุ Unicode

ภาษาไทยบางคำ (เช่นที่มี `ำ`) มีโอกาสพิมพ์คนละ Unicode form ได้ จึงมี alias สำรองบางชื่อเพื่อรองรับการใช้งานร่วมกัน

## ตัวอย่างการใช้งาน

ติดตั้งจาก PyPI:

```bash
pip install thaithon
```

จากนั้นสามารถ import โมดูลภาษาไทยได้ตรง ๆ เช่น:

```python
from ไพท่อน import พิมพ์, ความยาว
import คณิต
import เวลา
import สถิติ
import เจสัน

คะแนน = [12, 18, 20, 15]
ค่าเฉลี่ย = สถิติ.เฉลี่ย(คะแนน)
คะแนนรวม = คณิต.รวม(*คะแนน)
เวลาตอนนี้ = เวลา.เป็นข้อความไทย(เวลา.ตอนนี้())

สรุป = {
  "คะแนนรวม": คะแนนรวม,
  "ค่าเฉลี่ย": ค่าเฉลี่ย,
  "จำนวนรายการ": ความยาว(คะแนน),
  "เวลาประมวลผล": เวลาตอนนี้,
}

พิมพ์("สรุปผล:")
พิมพ์(เจสัน.แปลงเป็นข้อความ(สรุป, ย่อหน้า=2))
```

ถ้ารันจาก source code ใน repo นี้โดยตรง ให้เพิ่มโฟลเดอร์ `libs` เข้า `sys.path` ก่อน:

```python
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
if str(LIB_DIR) not in sys.path:
  sys.path.insert(0, str(LIB_DIR))

from ไพท่อน import พิมพ์
import เวลา

พิมพ์("ตอนนี้:", เวลา.เป็นข้อความ(เวลา.ตอนนี้()))
```

## วิธีรันตัวอย่าง

เปิด terminal ที่ root ของโปรเจกต์ แล้วรัน:

```bash
python examples/y.py
python examples/x.py
```

## วิธีรันเทส

```bash
python tests/test_data_libs.py
python tests/test_math.py
python tests/test_math_extended.py
python tests/test_datetime.py
python tests/test_random_stats.py
python tests/test_helpers.py
python tests/test_sleep.py
```

## เริ่มใช้งานกับ Git

โปรเจกต์นี้ถูกเตรียมโครงสร้างและไฟล์พื้นฐานสำหรับ Git แล้ว (`.gitignore`, `.gitattributes`, `.editorconfig`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`)

คำสั่งเริ่มต้นที่แนะนำ:

```bash
git status
git add .
git commit -m "chore: initialize Pythai project structure"
```

## Pre-package Checklist

ก่อนเริ่มทำเป็น package จริง แนะนำให้เช็ก:

- ตั้งชื่อ package ที่จะ publish (เช่น `pythai` หรือชื่อไทยแบบทับศัพท์)
- รวม API ที่ต้องการเปิด public ให้ชัดในแต่ละไฟล์ `__all__`
- ให้ test หลักผ่านทั้งหมด
- เก็บ changelog ให้เป็นเวอร์ชัน (`Unreleased` -> `x.y.z`)
- เลือกแนวทาง versioning (เช่น SemVer)

## เตรียมปล่อยขึ้น PyPI

โปรเจกต์นี้มีไฟล์ `pyproject.toml` แล้ว และสามารถ build ได้ด้วย PEP 517

1. Build package

```bash
python -m build
```

2. ตรวจสอบไฟล์ build

```bash
python -m twine check dist/*
```

3. ทดลองปล่อยขึ้น TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
```

4. ปล่อยขึ้น PyPI จริง

```bash
python -m twine upload dist/*
```

หมายเหตุ:
- เพิ่ม version ทุกครั้งก่อนปล่อย release ใหม่

## License และ Attribution

- โปรเจกต์นี้ใช้สัญญาอนุญาต Apache-2.0
- กรุณาเก็บไฟล์ `LICENSE` และ `NOTICE` ไว้เมื่อมีการแจกจ่ายต่อ
- หากใช้งานในงานวิจัย/บทความ แนะนำให้อ้างอิงจากไฟล์ `CITATION.cff`

## Credit

- Maintainer: OteEnded
- Contact: ratnaritjumnong@gmail.com

## แนวทาง naming

- ใช้คำไทยความหมายตรง เช่น `พิมพ์`, `รับค่า`, `จำนวนเต็ม`, `จำนวนจริง`
- ลดคำทับศัพท์เท่าที่ทำได้
- เก็บ compatibility alias ในกรณีที่จำเป็น