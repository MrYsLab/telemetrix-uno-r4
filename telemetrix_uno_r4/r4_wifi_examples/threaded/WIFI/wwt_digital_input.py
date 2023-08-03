"""
 Copyright (c) 2023 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,f
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

 DHT support courtesy of Martyn Wheeler
 Based on the DHTNew library - https://github.com/RobTillaart/DHTNew
"""

import sys
import time

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi
"""
Monitor a digital input pin
"""

"""
Setup a pin for digital input and monitor its changes
"""

# Set up a pin for analog input and monitor its changes
DIGITAL_PIN = 12  # arduino pin number

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

# variable to hold the last time a button state changed
debounce_time = time.time()


def the_callback(data):
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [pin, current reported value, pin_mode, timestamp]
    """
    global debounce_time

    # if the time from the last event change is > .2 seconds, the input is debounced
    if data[CB_TIME] - debounce_time > .3:
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
        print(f'Pin: {data[CB_PIN]} Value: {data[CB_VALUE]} Time Stamp: {date}')
        debounce_time = data[CB_TIME]


def digital_in(my_board, pin):
    """
     This function establishes the pin as a
     digital input. Any changes on this pin will
     be reported through the call back function.

     :param my_board: a telemetrix instance
     :param pin: Arduino pin number
     """

    # set the pin mode
    my_board.set_pin_mode_digital_input(pin, the_callback)
    # time.sleep(1)
    # my_board.disable_all_reporting()
    # time.sleep(4)
    # my_board.enable_digital_reporting(12)

    # time.sleep(3)
    # my_board.enable_digital_reporting(pin)
    # time.sleep(1)

    print('Enter Control-C to quit.')
    # my_board.enable_digital_reporting(12)
    try:
        while True:
            time.sleep(.0001)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)


board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_address='192.168.2.118')
try:
    digital_in(board, DIGITAL_PIN)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
