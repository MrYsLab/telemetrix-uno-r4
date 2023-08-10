## Setting Pin Modes

Pin modes must be set before interacting with a pin. All the methods listed
below have a consistent API across all API classes.

### Input Pin Modes

#### Requiring A Callback To Be Specified
* set_pin_mode_analog_input
* set_pin_mode_dht
* set_pin_mode_digital_input
* set_pin_mode_digital_input_pullup
* set_pin_mode_sonar

#### Callback Specified In Read Commands
* set_pin_mode_i2c
* set_pin_mode_spi

### Output Pin Modes
* set_pin_mode_analog_output
* set_pin_mode_digital_output
* set_pin_mode_servo



<br>
<br>

Copyright (C) 2023 Alan Yorinks. All Rights Reserved.