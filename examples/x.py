from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT_DIR / "libs"
if str(LIB_DIR) not in sys.path:
	sys.path.insert(0, str(LIB_DIR))

from ไพทอน import *

เอ็กซ์ = รับค่า("ป้อนค่า x: ")

พิมพ์("ค่าที่ป้อนคือ:", เอ็กซ์)