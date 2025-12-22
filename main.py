import os, sys, io
import M5
from M5 import *
from hardware import RGB


PIXEL_NUM = 24
rgb = None


def setup():
    global rgb

    M5.begin()
    Widgets.setRotation(0)
    Widgets.fillScreen(0x000000)

    rgb = RGB(io=26, n=PIXEL_NUM, type="WS2812")  # Neopixel


def shift_color(c, arr):
    arr.insert(0, c)
    if len(arr) > PIXEL_NUM:
        arr.pop()
    for i, c in enumerate(arr):
        rgb.set_color(i, c)


def loop():
    M5.update()
    arr = []
    while True:
        ax, ay, az = Imu.getAccel()
        c = int(256 * abs(ax) / 2)
        c *= 256
        c = int(256 * abs(ay) / 2)
        c *= 256
        c = int(255 * abs(az) / 2)
        shift_color(c, arr)


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
