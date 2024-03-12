## Arduino Compiler Warnings
Telemetrix4UnoR4 uses the NewPing library for HC-SR04 Sonar distance sensor support.
You may see the following warning when compiling any of the servers.
This warning may be safely ignored.

An [issue](https://bitbucket.org/teckel12/arduino-new-ping/issues/78/add-renesas_uno-to-libraryproperties) was created but has not yet been addressed.


```angular2html
WARNING: library NewPing claims to run on avr, megaavr, esp32 architecture(s)
and may be incompatible with your current board which runs on 
renesas architecture(s).

```

## BLE

### Client Side Issues
BLE is only supported using the [asyncio API](telemetrix_wifi_reference_aio.md). The 
threaded API does not support BLE.


<br>