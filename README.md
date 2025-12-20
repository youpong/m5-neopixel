# StartSignal
A sample project that drives NeoPixels using the M5StickC Plus by M5Stack Technology.

## Development Environment
This program runs in MicroPython within the [UiFlow2](https://uiflow2.m5stack.com).

## Setup
### Install USB Driver
* Install the FTDI driver.

### Burn Firmware
* Install M5Burner.
* Burn firmware.

### Add RGB Hardware
In UiFlow2, add RGB hardware.

### Edit main.py

Modify the following constants to match your NeoPixel device. For example, if
the number of NeoPixels is 8:
```python
PIXEL_NUM = 8
```

### Download the program
* Using UiFlow2, download the program to the M5StickC Plus.

### Connect the M5StickC Plus and NeoPixel
connect as follows.

| M5StickC Plus | NeoPixel |
|---------------|----------|
| GND           | GND |
| 5V            | VCC |
| G26           | DIN |

## Setting up a Python Development Environment

### Create and activate virtual environment(venv)
```bash
# create virtual environment
$ python -m venv .venv
# activate for Windows
$ .venv/bin/activate 
# activate for macOS / Linux
$ source .venv/bin/activate
```

### To Upgrade pip [if necessary]
```bash
$ pip install --upgrade pip
```

### Installing development dependency packages
```bash
$ pip install -r requirements-dev.txt
```

### format source files
```bash
$ black source_files...
```

### Linting source files
```bash
$ flake8 source_files...
```

## References
* https://github.com/youpong/mb-neopixel - A similar project for the BBC micro:bit

## License

MIT