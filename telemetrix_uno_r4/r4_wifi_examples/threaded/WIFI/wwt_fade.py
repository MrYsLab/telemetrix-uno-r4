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


"""

import sys
import time

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi

"""
Setup a pin for output and fade its intensity
"""

# some globals
# make sure to select a PWM pin
DIGITAL_PIN = 13

# Create a Telemetrix instance.
board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_address='192.168.2.118')

# Set the DIGITAL_PIN as an output pin
board.set_pin_mode_analog_output(DIGITAL_PIN)
# board.set_pin_mode_analog_output(DIGITAL_PIN)


# When hitting control-c to end the program
# in this loop, we are likely to get a KeyboardInterrupt
# exception. Catch the exception and exit gracefully.

try:
    print('Fading up...')
    for i in range(255):
        board.analog_write(DIGITAL_PIN, i)
        time.sleep(.005)
    print('Fading down...')
    for i in range(255, -1, -1):
        board.analog_write(DIGITAL_PIN, i)
        time.sleep(.005)

    board.set_pin_mode_digital_output(DIGITAL_PIN)

except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
