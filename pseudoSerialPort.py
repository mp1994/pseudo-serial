#!/usr/bin/env python3

import os, pty, time, sys


if __name__=='__main__':

    master,slave = pty.openpty()  # open the pseudoterminal
    s_name = os.ttyname(slave)    # translate the slave fd to a filename
    print("Connect to: \033[1;33m{}\033[0m".format(s_name))

    try:        
        s = input("\nPress any key to start...")
    except KeyboardInterrupt:
        print("\n")
        exit(0)

    print("\033[1;32m [INFO]\033[0m Simulating the serial port...")
    
    drr = float(sys.argv[1]) if len(sys.argv)>1 else 50
    dt = 1.0/drr
    print("\033[1;32m [INFO]\033[0m Data refresh rate: {:.2f} Hz".format(drr))

    counter = 0
    TxBuffer = bytearray(9)
    TxBuffer[-1] = ord('\r')
    
    while 1:
        counter = counter+1
        TxBuffer[0:4] = counter.to_bytes(4, sys.byteorder)
        os.write(master, TxBuffer)
        time.sleep(dt) 
