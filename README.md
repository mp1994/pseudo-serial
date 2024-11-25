# Pseudo serial port

This repo contains a simple Python script that emulates a serial device sending out data over its serial port.

### Usage

Launch the Python script:

``` bash
$ ./pseudoSerialPort.py
Connect to /dev/pts/6

Press any key to start...
```

From any other terminal/application, open the serial port show in the log above (i.e., `/dev/pts/6`) and you should see packets incoming at 50 Hz (default data rate of the pseudo-serial device).

Customize the Python script to best fit your needs.