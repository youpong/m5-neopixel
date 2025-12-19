import os, sys, io
import M5
from M5 import *
from hardware import RGB


rgb26 = None
tuple0 = None


def setup():
  global rgb26, tuple0

  M5.begin()
  Widgets.setRotation(0)
  Widgets.fillScreen(0x000000)

  rgb26 = RGB(io=26, n=24, type="WS2812")


def shift_color(c, arr):
  print(c)
  arr[:] = [c] + arr[:-1]
  for i, c in enumerate(arr):
    rgb26.set_color(i, c)


def loop():
  global rgb26, tuple0
  M5.update()
  arr = [0] * 24
  while True:
    ax, ay, az = Imu.getAccel()
    c = int(255 * abs(ax) / 2)
    c = int(c * 256 + 255 * abs(ay) / 2)
    c = int(c * 256 + 255 * abs(az) / 2)
    shift_color(c, arr)


if __name__ == '__main__':
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
