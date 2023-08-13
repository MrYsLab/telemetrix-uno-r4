Here, we need to instantiate the class passing in two parameters.
We need to pass in auto_start=False. This is because we are using the Bleak BLE 
library, and this allows for a clean shutdown.
We also need to pass in transport_type=2, which enables the BLE transport.

Lastly, we need to manually start the asyncio portion of the API by calling
board.start_aio() in our main function.

```angular2html

import sys
import asyncio

# IMPORT THE API
from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi_aio import telemetrix_uno_r4_wifi_aio

# An async method for running your application.
# We pass in the instance of the API created below .
async def my_app(my_board):
    # THIS NEXT LINE MUST BE ADDED HERE
    await my_board.start_aio()

    # Your Application code

# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# instantiate telemetrix_aio

board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(autostart=False,
                                                          transport_type=2)

try:
    # start the main function
    loop.run_until_complete(my_app(board))
except KeyboardInterrupt:
    try:
        loop.run_until_complete(board.shutdown())
    except:
        pass
    sys.exit(0)

```

<br>
