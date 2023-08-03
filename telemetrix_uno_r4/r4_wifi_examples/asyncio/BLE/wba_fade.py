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
import asyncio

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi_aio import telemetrix_uno_r4_wifi_aio
"""
Setup a pin for output and fade its intensity
"""

# some globals
# make sure to select a PWM pin
DIGITAL_PIN = 13


async def fade(the_board, pin):
    await the_board.start_aio()
    # Set the DIGITAL_PIN as an output pin
    await the_board.set_pin_mode_analog_output(pin)

    # When hitting control-c to end the program
    # in this loop, we are likely to get a KeyboardInterrupt
    # exception. Catch the exception and exit gracefully.

    try:
        print('Fading up...')
        for i in range(255):
            await the_board.analog_write(DIGITAL_PIN, i)
            await asyncio.sleep(.009)
        print('Fading down...')
        for i in range(255, -1, -2):
            await the_board.analog_write(DIGITAL_PIN, i)
            await asyncio.sleep(.009)
        await asyncio.sleep(4)
        await the_board.shutdown()
    except KeyboardInterrupt:
        await the_board.shutdown()
    except Exception as e:
        await the_board.shutdown()

# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# instantiate telemetrix_aio
board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(autostart=False,
                                                          transport_type=2)
try:
    # start the main function
    loop.run_until_complete(fade(board, DIGITAL_PIN))
except KeyboardInterrupt:
    try:
        loop.run_until_complete(board.shutdown())
    except:
        pass