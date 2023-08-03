import asyncio
import sys
import time

from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi_aio import telemetrix_uno_r4_wifi_aio

"""
Establishing a digital and analog input pin and monitoring their values.
"""


class PinsWithinClass:
    def __init__(self, board, d_pin, a_pin):
        """

        :param board: a telemetrix aio instance
        :param d_pin: digital input pin number
        :param a_pin: analog input pin number

        """
        self.board = board
        self.d_pin = d_pin
        self.a_pin = a_pin

        self.last_analog_value = 0

    async def run_it(self):
        """
        Initialize pin modes with the callbacks
        """

        await self.board.set_pin_mode_digital_input(self.d_pin, callback=self.callback)
        await self.board.set_pin_mode_analog_input(self.a_pin,
                                                   differential=3, callback=self.callback)

    async def callback(self, data):
        """

        :param data: data[0] = report type 2 = digital input
                               report type 3 = analog input
                     data[1] = pin number
                     data[2] = reported value
        """
        if data[0] == 2:
            if data[2] == self.last_analog_value:
                pass
            else:
                self.last_analog_value = data[2]
                print(f'digital input pin {data[1]} reports a value of {data[2]}')
        elif data[0] == 3:
            print(f'analog input pin {data[1]} reports a value of {data[2]}')


# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# instantiate telemetrix_aio
the_board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(
    transport_address='192.168.2.118')


async def monitor(my_board, digital_pin, analog_pin):
    """
    Set the pin modes for the pins

    :param my_board: telemetrix aio instance
    :param digital_pin: Arduino digital input pin number
    :param analog_pin: Arduino analog input pin number

    """

    pwc = PinsWithinClass(my_board, digital_pin, analog_pin)
    await pwc.run_it()
    # wait forever
    while True:
        try:
            await asyncio.sleep(.00001)
        except KeyboardInterrupt:
            await my_board.shutdown()
            sys.exit(0)


try:
    # start the main function
    loop.run_until_complete(monitor(the_board, 12, 2))
except KeyboardInterrupt:
    loop.run_until_complete(the_board.shutdown())
    sys.exit(0)
