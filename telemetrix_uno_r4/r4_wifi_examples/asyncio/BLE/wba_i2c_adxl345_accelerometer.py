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
This example sets up and control an ADXL345 i2c accelerometer.
It will continuously print data the raw xyz data from the device.
"""


# the call back function to print the adxl345 data
async def the_callback(data):
    """

    :param data: [pin_type, Device address, device read register, x data pair, y data pair, z data pair]
    :return:
    """
    report_type = data[0]
    number_bytes_read = data[2]
    i2c_device_address = data[3]
    i2c_register = data[4]
    x_msb = data[5]
    x_lsb = data[6]
    y_msb = data[7]
    y_lsb = data[8]
    z_msb = data[9]
    z_lsb = data[10]

    x_data = (x_msb << 8) + x_lsb
    y_data = (y_msb << 8) + y_lsb
    z_data = (z_msb << 8) + z_lsb

    # test report type for SPI report
    if report_type == 10:
        print(f'i2c Report:   i2c device address: {i2c_device_address}    i2c '
              f'Register: '
              f'{i2c_register}   Number Of Bytes Read: {number_bytes_read}    x: '
              f'{x_data}   y: {y_data}   z: {z_data}')
    else:
        print(f'unexpected report type: {report_type}')


async def adxl345(my_board):
    await my_board.start_aio()
    # setup adxl345
    # device address = 83
    await my_board.set_pin_mode_i2c()

    # set up power and control register
    await my_board.i2c_write(83, [45, 0])
    await asyncio.sleep(.1)
    await my_board.i2c_write(83, [45, 8])
    await asyncio.sleep(.1)

    # set up the data format register
    await my_board.i2c_write(83, [49, 8])
    await asyncio.sleep(.1)
    await my_board.i2c_write(83, [49, 3])
    await asyncio.sleep(.1)

    # read_count = 20
    while True:
        # read 6 bytes from the data register
        try:
            await my_board.i2c_read(83, 50, 6, the_callback)
            await asyncio.sleep(.5)

        except (KeyboardInterrupt, RuntimeError):
            await my_board.shutdown()
            sys.exit(0)

# instantiate telemetrix_aio
board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(autostart=False,
                                                          transport_type=2)
# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

try:
    # start the main function
    loop.run_until_complete(adxl345(board))
except KeyboardInterrupt:
    try:
        loop.run_until_complete(board.shutdown())
    except:
        pass
    sys.exit(0)
