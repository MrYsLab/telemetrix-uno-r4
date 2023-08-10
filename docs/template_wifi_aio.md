Here, we need to instantiate the class passing in the IP address assigned by your 
router. This parameter enables the WIFI transport.

```angular2html

import sys
import asyncio

# IMPORT THE API
from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi_aio import telemetrix_uno_r4_wifi_aio

# An async method for running your application.
# We pass in the instance of the API created below .
async def my_app(the_board):
    # Your Application code

# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# instantiate telemetrix_aio
# Make sure to edit the transport address assigned by your router.
board = telemetrix_uno_r4_wifi_aio.TelemetrixUnoR4WiFiAio(
    transport_address='192.168.2.118')

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
<br>

Copyright (C) 2023 Alan Yorinks. All Rights Reserved.