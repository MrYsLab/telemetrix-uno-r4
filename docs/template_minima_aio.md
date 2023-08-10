```angular2html

import sys
import asyncio

# IMPORT THE API
from telemetrix_uno_r4.minima.telemetrix_uno_r4_minima_aio import telemetrix_uno_r4_minima_aio

# An async method for running your application.
# We pass in the instance of the API created below .
async def my_app(the_board):
    # Your Application code

# get the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# instantiate telemetrix_aio
board = telemetrix_uno_r4_minima_aio.TelemetrixUnoR4MinimaAio()

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