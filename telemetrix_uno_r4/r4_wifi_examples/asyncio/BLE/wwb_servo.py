"""
 Copyright (c) 2023 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import asyncio
import sys

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi_aio import telemetrix_uno_r4_wifi_aio

"""
This example will set a servo to 0, 90 and 180 degree
positions.
"""


async def servo(my_board, pin):
    """
    Set a pin to servo mode and then adjust
    its position.

    :param my_board: telemetrix_aio instance
    :param pin: pin to be controlled
    """
    await my_board.start_aio()

    # set the pin mode
    await my_board.set_pin_mode_servo(pin)

    await asyncio.sleep(1)

    await my_board.servo_write(pin, 0)
    await asyncio.sleep(1)
    await my_board.servo_write(pin, 90)
    await asyncio.sleep(1)
    await my_board.servo_write(pin, 180)
    await my_board.servo_detach(pin)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(autostart=False,
                                                          transport_type=2)
try:
    loop.run_until_complete(servo(board, 5))
    try:
        loop.run_until_complete(board.shutdown())
    except:
        pass
    sys.exit(0)
except KeyboardInterrupt:
    try:
        loop.run_until_complete(board.shutdown())
    except:
        pass
    sys.exit(0)
