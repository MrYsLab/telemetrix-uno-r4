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

import sys
import time

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi

"""
This program monitors a DHT22 sensor.
"""

# Arduino pin number
DHT_PIN = 8

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


# A callback function to display the distance
# noinspection GrazieInspection
def the_callback(data):
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


def dht(my_board, pin, callback, dht_type):
    # noinspection GrazieInspection
    """
        Set the pin mode for a DHT 22 device. Results will appear via the
        callback.

        :param my_board: an telemetrix instance
        :param pin: Arduino pin number
        :param callback: The callback function
        :param dht_type: 22 or 11
        """

    # set the pin mode for the DHT device
    my_board.set_pin_mode_dht(pin, callback=callback, dht_type=dht_type)


board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_address='192.168.2.118')
try:
    dht(board, DHT_PIN, the_callback, 11)

    # wait forever
    while True:
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            board.shutdown()
            sys.exit(0)
except (KeyboardInterrupt, RuntimeError):
    board.shutdown()
    sys.exit(0)
