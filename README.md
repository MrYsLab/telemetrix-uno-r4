## telemetrix-uno-r4

# Telemetrix For The Arduino UNO R4 Minima and WIFI


This Python package allows you to monitor and control an UNO R4 Minima or 
WIFI board by simply writing a Python script using one of the telemetrix--uno-r4 APIs.
APIs are provided for both synchronous and asyncio implementations.

| Feature                            | Minima | WIFI | Notes |
|------------------------------------|:------:|:----:|:-----:|
| Analog Input                       |   X    |  X   |       |
| Analog Output (PWM)                |   X    |  X   |       |
| Digital Input                      |   X    |  X   |       |
| Digital Output                     |   X    |  X   |       |
| i2c Primitives                     |   X    |  X   |       |
| Servo Motor Control                |   X    |  X   |       |
| DHT Temperature/Humidity Sensor    |   X    |  X   |       |
| HC-SR04 Sonar Distance Sensor      |   X    |  X   |       |
| SPI Primitives                     |   X    |  X   |       |
| Scrolling Message Support          |        |  X   |       |
| Integrated Debugging Aids Provided |   X    |  X   |       |
| Examples ProvidedFor All Features  |   X    |  X   |       |

For the Minima, communication with the Python client is supported by a USBSerial 
transport.

For the WIFI board, you may choose a WIFI, USBSerial or BLE transport. The transport 
type is identified on the LED display.

Please refer to the [User's Guide](https://mryslab.github.io/telemetrix-uno-r4/) for further information, including installation 
instructions and client APIs.

Programmed with [Pycharm](https://www.jetbrains.com/pycharm/)  ![](https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm_icon.svg)