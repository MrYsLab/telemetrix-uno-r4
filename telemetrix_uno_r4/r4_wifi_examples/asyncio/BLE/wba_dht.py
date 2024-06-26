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
import time

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi_aio import telemetrix_uno_r4_wifi_aio

"""
This program monitors two DHT22 and two DHT11 sensors.
"""


# indices into callback data for valid data
# REPORT_TYPE = 0
# READ_RESULT = 1
# PIN = 2
# DHT_TYPE = 3
# HUMIDITY = 4
# TEMPERATURE = 5
# TIME = 6

# indices into callback data for error report
# REPORT_TYPE = 0
# READ_RESULT = 1
# PIN = 2
# DHT_TYPE = 3
# TIME = 4

# Arduino Pin Number
DHT_PIN = 8


# A callback function to display the distance
# noinspection GrazieInspection
async def the_callback(data):
    # noinspection GrazieInspection
    """
        The callback function to display the change in distance
        :param data: [report_type = PrivateConstants.DHT, error = 0, pin number,
        dht_type, humidity, temperature timestamp]
                     if this is an error report:
                     [report_type = PrivateConstants.DHT, error != 0, pin number, dht_type
                     timestamp]
        """
    if data[1]:
        # error message
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[4]))
        print(f'DHT Error Report:'
              f'Pin: {data[2]} DHT Type: {data[3]} Error: {data[1]}  Time: {date}')
    else:
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[6]))
        print(f'DHT Valid Data Report:'
              f'Pin: {data[2]} DHT Type: {data[3]} Humidity: {data[4]} Temperature:'
              f' {data[5]} Time: {date}')


async def dht(my_board, pin):
    # noinspection GrazieInspection
    """
        Set the pin mode for a DHT 22 device. Results will appear via the
        callback.

        :param my_board: a telemetrix instance

        :param pin: DHT data pin

        """
    await my_board.start_aio()
    # set the pin mode for a DHT 11 or 22
    await my_board.set_pin_mode_dht(pin, the_callback, dht_type=22)

    # just sit in a loop waiting for the reports to come in
    while True:
        try:
            await asyncio.sleep(.001)
        except KeyboardInterrupt:
            my_board.shutdown()
            sys.exit(0)

# instantiate telemetrix_aio
# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# instantiate telemetrix_aio
board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(autostart=False,
                                                          transport_type=2)

try:
    # start the main function
    loop.run_until_complete(dht(board, DHT_PIN))
except KeyboardInterrupt:
    try:
        loop.run_until_complete(board.shutdown())
    except:
        pass
    sys.exit(0)

