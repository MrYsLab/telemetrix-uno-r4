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
from telemetrix_uno_r4.minima.telemetrix_uno_r4_minima import telemetrix_uno_r4_minima

"""
This example sets up and control an ADXL345 i2c accelerometer.
It will continuously print data the raw xyz data from the device.
"""


# the call back function to print the adxl345 data
def the_callback(data):
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
        print(f'i2c Report:   i2c device address: {i2c_device_address  }    i2c '
              f'Register: '
              f'{i2c_register}   Number Of Bytes Read: {number_bytes_read}    x: '
              f'{x_data}   y: {y_data}   z: {z_data}')
    else:
        print(f'unexpected report type: {report_type}')


def adxl345(my_board):
    # setup adxl345
    # device address = 83
    my_board.set_pin_mode_i2c()

    # set up power and control register
    my_board.i2c_write(83, [45, 0])
    time.sleep(.1)
    my_board.i2c_write(83, [45, 8])
    time.sleep(.1)

    # set up the data format register
    my_board.i2c_write(83, [49, 8])
    time.sleep(.1)
    my_board.i2c_write(83, [49, 3])
    time.sleep(.1)

    # read_count = 20
    while True:
        # read 6 bytes from the data register
        try:
            my_board.i2c_read(83, 50, 6, the_callback)
            time.sleep(.1)

        except (KeyboardInterrupt, RuntimeError):
            my_board.shutdown()
            sys.exit(0)


board = telemetrix_uno_r4_minima.TelemetrixUnoR4Minima()

try:
    adxl345(board)
except KeyboardInterrupt:
    try:
        board.shutdown()
    except:
        pass
    sys.exit(0)
