# SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

import os, sys, io
import M5
from M5 import *
from module import LoRa868V12Module
import time


title0 = None
label_t = None
label_time = None
label_tx = None
label_ts = None
lora868v12_0 = None
count = None
last_time = None
timestamp = None


def setup():
    global \
        title0, \
        label_t, \
        label_time, \
        label_tx, \
        label_ts, \
        lora868v12_0, \
        count, \
        last_time, \
        timestamp

    M5.begin()
    Widgets.fillScreen(0x222222)
    title0 = Widgets.Title("LoRa Module Tx", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    label_t = Widgets.Label("Send:", 5, 50, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    label_time = Widgets.Label("1", 118, 150, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    label_tx = Widgets.Label("hello", 65, 50, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    label_ts = Widgets.Label("timestamp:", 5, 150, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)

    count = 0
    lora868v12_0 = LoRa868V12Module(
        pin_rst=5,
        pin_cs=1,
        pin_irq=10,
        pin_busy=2,
        freq_khz=868000,
        bw="250",
        sf=8,
        coding_rate=8,
        preamble_len=12,
        syncword=0x12,
        output_power=10,
    )
    last_time = time.ticks_ms()


def loop():
    global \
        title0, \
        label_t, \
        label_time, \
        label_tx, \
        label_ts, \
        lora868v12_0, \
        count, \
        last_time, \
        timestamp
    M5.update()
    if (time.ticks_diff((time.ticks_ms()), last_time)) >= 1000:
        last_time = time.ticks_ms()
        count = count + 1
        timestamp = lora868v12_0.send((str("hello M5 ") + str(count)), None)
        label_tx.setText(str((str("hello M5 ") + str(count))))
        label_time.setText(str(last_time))


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
