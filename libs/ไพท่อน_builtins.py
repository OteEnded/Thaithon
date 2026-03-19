from builtins import abs as ค่าสัมบูรณ์
from builtins import all as ทั้งหมดจริง
from builtins import any as มีสักอันจริง
from builtins import bin as ฐานสอง
from builtins import bool as ค่าความจริง
from builtins import dict as พจนานุกรม
from builtins import dir as ดูรายชื่อ
from builtins import divmod as หารเอาเศษพร้อมส่วน
from builtins import enumerate as ลำดับ
from builtins import filter as กรอง
from builtins import float as จำนวนจริง
from builtins import format as จัดรูปแบบ
from builtins import getattr as อ่านคุณสมบัติ
from builtins import hasattr as มีคุณสมบัติไหม
from builtins import help as ช่วย
from builtins import hex as ฐานสิบหก
from builtins import input as รับค่า
from builtins import int as จำนวนเต็ม
from builtins import isinstance as เป็นชนิดเดียวกันไหม
from builtins import issubclass as เป็นคลาสลูกไหม
from builtins import len as ความยาว
from builtins import list as รายการ
from builtins import map as แปลงทีละตัว
from builtins import max as สูงสุด
from builtins import min as ต่ำสุด
from builtins import oct as ฐานแปด
from builtins import open as เปิดไฟล์
from builtins import pow as ยกกำลัง
from builtins import print as พิมพ์
from builtins import range as ช่วง
from builtins import reversed as กลับลำดับ
from builtins import round as ปัดเศษ
from builtins import set as กลุ่มไม่ซ้ำ
from builtins import setattr as ตั้งคุณสมบัติ
from builtins import sorted as เรียงแล้ว
from builtins import str as ข้อความ
from builtins import sum as รวม
from builtins import tuple as ชุดข้อมูลคงที่
from builtins import type as ชนิด
from builtins import zip as จับคู่

บูลีน = ค่าความจริง
ดิก = พจนานุกรม
ทศนิยม = จำนวนจริง
อินพุต = รับค่า
อินท์ = จำนวนเต็ม
ลิสต์ = รายการ
แมป = แปลงทีละตัว
ปริ้น = พิมพ์
เซต = กลุ่มไม่ซ้ำ
ทูเพิล = ชุดข้อมูลคงที่


def เรียงลำดับ(ข้อมูล, *, key=None, reverse=False):
    ข้อมูล.sort(key=key, reverse=reverse)
    return ข้อมูล


จริง = True
เท็จ = False
ไม่มี = None

จํานวนจริง = จำนวนจริง
จํานวนเต็ม = จำนวนเต็ม
เรียงลําดับ = เรียงลำดับ

__all__ = [
    "ค่าสัมบูรณ์",
    "ความยาว",
    "ข้อความ",
    "จริง",
    "จับคู่",
    "จัดรูปแบบ",
    "จํานวนจริง",
    "จํานวนเต็ม",
    "จำนวนจริง",
    "จำนวนเต็ม",
    "ช่วย",
    "ชนิด",
    "ช่วง",
    "ตั้งคุณสมบัติ",
    "ฐานสอง",
    "ฐานแปด",
    "ฐานสิบหก",
    "พจนานุกรม",
    "พิมพ์",
    "ต่ำสุด",
    "ทั้งหมดจริง",
    "เท็จ",
    "ดูรายชื่อ",
    "ปัดเศษ",
    "เปิดไฟล์",
    "เป็นชนิดเดียวกันไหม",
    "เป็นคลาสลูกไหม",
    "ค่าความจริง",
    "ไม่มี",
    "มีคุณสมบัติไหม",
    "มีสักอันจริง",
    "ยกกำลัง",
    "รายการ",
    "รวม",
    "ลำดับ",
    "สูงสุด",
    "ชุดข้อมูลคงที่",
    "อ่านคุณสมบัติ",
    "รับค่า",
    "กรอง",
    "กลุ่มไม่ซ้ำ",
    "กลับลำดับ",
    "หารเอาเศษพร้อมส่วน",
    "แปลงทีละตัว",
    "เรียงแล้ว",
    "เรียงลําดับ",
    "เรียงลำดับ",
]