# Installing The Client APIs

## Installing For The First Time
To install from PyPI, within your virtual environment type:

```bash
pip install telemetrix-uno-r4
```

## Upgrading To A Newer Version
To upgrade to a newer version from an existing installation, use the following command:

```angular2html
pip install telemetrix-uno-r4 --upgrade

```

## What Is Installed?
The telemetrix-uno-r4 package contains four client APIs. You have the choice of using 
an API employing a threaded concurrency model or an API using an asyncio concurrency 
model.  The asyncio API 
names end 
with _\_aio_. 

**NOTE**: BLE is only supported by telemetrix_uno_r4_wifi_aio.

### Arduino UNO R4 Mimima Clients

  * [telemetrix_uno_r4_minima](telemetrix_minima_reference.md)

  * [telemetrix_uno_r4_minima_aio ](telemetrix_minima_reference_aio.md)


### Arduino UNO R4 WIFI Clients
  * [telemetrix_uno_r4_wifi](telemetrix_wifi_reference.md)

  * [telemetrix_uno_r4_wifi_aio](telemetrix_wifi_reference_aio.md) 


<br>
