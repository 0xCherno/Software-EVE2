from pyfirmata2 import Arduino
import time

board = Arduino(Arduino.AUTODETECT)
board.samplingOn(10)

alpha = 0.1
digital_pins = [board.get_pin(f"")]