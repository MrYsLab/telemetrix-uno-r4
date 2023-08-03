
"""
 Copyright (c) 2020-2023 Alan Yorinks All rights reserved.

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
import bleak

from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"


class TelemetrixAioBle:
    """
    This class encapsulates management of a BLE UART connection that communicates
    with an Arduino UNO R4 WIFI
    """
    def __init__(self, ble_device_name, receive_notification_callback):
        self.ble_device_name = ble_device_name
        self.receive_notification_callback = receive_notification_callback
        self.ble_device = None
        self.bleak_client = None
        self.nus = None
        self.rx_char = None
        self.tx_char = None

    async def connect(self):
        """
        This method connects to a device matching the ble_device_name

        :return:
        """
        print(f'Scanning for BLE device {self.ble_device_name}.  Please wait...')

        self.ble_device = await BleakScanner.find_device_by_name(self.ble_device_name)
        if self.ble_device is None:
            raise RuntimeError('Did not find the BLE device. Please check name.')
        print(f'Found  {self.ble_device_name}  address: {self.ble_device.address}')
        self.bleak_client = BleakClient(self.ble_device.address)
        await self.bleak_client.connect()
        await self.bleak_client.start_notify(UART_TX_CHAR_UUID,
                                             self.receive_notification_callback)

    async def write(self, data):
        """
        This method writes data to the IP device
        :param data:

        :return: None
        """
        await self.bleak_client.write_gatt_char(UART_RX_CHAR_UUID, data)
