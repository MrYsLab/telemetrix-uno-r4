Here, we need to instantiate the class passing in the IP address assigned by your 
router. This parameter enables the WIFI transport.

```angular2html
import sys
import time

# IMPORT THE API
from telemetrix_uno_r4.wifi.telemetrix_uno_r4_wifi import telemetrix_uno_r4_wifi

# INSTANTIATE THE API CLASS
# Make sure to edit the transport address assigned by your router.

board = telemetrix_uno_r4_wifi.TelemetrixUnoR4WiFi(transport_address='192.168.2.118')
try:
    # WRITE YOUR APPLICATION HERE
except:
    board.shutdown()




```

<br>
<br>

Copyright (C) 2023 Alan Yorinks. All Rights Reserved.