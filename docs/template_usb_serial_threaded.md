Here, we need to instantiate the class passing in a transport_type of 1. This enables 
the serial transport.

```angular2html
import sys
import time

# IMPORT THE API
from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi

# INSTANTIATE THE API CLASS
board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_type=1)
try:
    # WRITE YOUR APPLICATION HERE
except:
    board.shutdown()




```

<br>
<br>

Copyright (C) 2023 Alan Yorinks. All Rights Reserved.