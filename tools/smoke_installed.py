#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import คณิต
import เวลา
import เจสัน

print("imports:", คณิต.__name__, เวลา.__name__, เจสัน.__name__)
print("math:", คณิต.ปัดขึ้น(3.2))
print("sleep_exists:", hasattr(เวลา, "นอน"))
print("json:", เจสัน.แปลงจากข้อความ('{"a": 1}'))
