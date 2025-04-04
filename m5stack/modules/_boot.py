# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import gc
import vfs
import os
from flashbdev import sys_bdev, vfs_bdev
import esp32

uiflow_str = f"""
       _  __ _               
 _   _(_)/ _| | _____      __
| | | | | |_| |/ _ \ \ /\ / /
| |_| | |  _| | (_) \ V  V / 
 \__,_|_|_| |_|\___/ \_/\_/  {esp32.firmware_info()[3]}
"""
print(uiflow_str)
del uiflow_str

# monut flash file system
try:
    if sys_bdev:
        # fs_sys = os.VfsLfs2(sys_bdev, progsize=32, readsize=128, lookahead=128)
        vfs.mount(sys_bdev, "/system")
    if vfs_bdev:
        # fs_vfs = os.VfsLfs2(vfs_bdev, progsize=32, readsize=128, lookahead=128)
        vfs.mount(vfs_bdev, "/flash")
except OSError:
    import inisetup

    inisetup.setup()

gc.collect()
gc.threshold(56 * 1024)

import micropython
import sys

micropython.alloc_emergency_exception_buf(256)
# system path
sys.path.append("/system")
sys.path.append("/flash/libs")

# change directory to "/flash"
os.chdir("/flash")

# copy OTA update file to main.py
# main_ota_temp.py this file name is fixed
try:
    s = open("/flash/main_ota_temp.py", "rb")
    f = open("/flash/main.py", "wb")
    f.write(s.read())
    s.close()
    f.close()
    os.remove("/flash/main_ota_temp.py")
except:
    pass
