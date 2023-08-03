"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

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


"""

import sys
import time

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi

"""
Setup a pin for digital output 
and toggle the pin 5 times.
"""

# some globals
message = 'Hello World'

# Create a Telemetrix instance.
board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_address='192.168.2.118')

try:
    # Set the DIGITAL_PIN as an output pin
    board.enable_scroll_message(message)
    time.sleep(5)
    board.disable_scroll_message()
    time.sleep(5)
    board.shutdown()
    sys.exit(0)
except:
    board.shutdown()
    sys.exit(0)

