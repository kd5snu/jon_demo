#!/usr/bin/python

from __future__ import division
import time
import math
import sys

import opc
#import color_utils

fps = 30         # frames per second
density = 144
length = 3.0

n_pixels = density * length
pulse_width = n_pixels / 6.
increment_val = pulse_width / 180.


#-------------------------------------------------------------------------------
# handle command line

if len(sys.argv) == 1:
    IP_PORT = '127.0.0.1:7890'
elif len(sys.argv) == 2 and ':' in sys.argv[1] and not sys.argv[1].startswith('-'):
    IP_PORT = sys.argv[1]
else:
    print('''
Usage: raver_plaid.py [ip:port]

If not set, ip:port defauls to 127.0.0.1:7890
''')
    sys.exit(0)


#-------------------------------------------------------------------------------
# connect to server
#def server_connect():
client = opc.Client(IP_PORT)
if client.can_connect():
    print('    connected to %s' % IP_PORT)
else:
    # can't connect, but keep running in case the server appears later
    print('    WARNING: could not connect to %s' % IP_PORT)
print('')


#-------------------------------------------------------------------------------
# send pixels

print('    sending pixels forever (control-c to exit)...')
print('')


#generate white fade
start_pixel = -(pulse_width)
#current_val = 0.0
r = 0
g = 0
b = 0

#### WHITE ####################

for run in range( int(n_pixels + pulse_width) ):
    pixels = []
    for current_pixel in range(int(n_pixels)):
        if( (current_pixel >= start_pixel) and (current_pixel < start_pixel + pulse_width) ):
            r = g = b = int(256*(math.sin(math.radians( start_pixel +
                                                        pulse_width -
                                                        current_pixel )/ increment_val)))
        else:
            r = g = b = 0
        print r
        pixels.append((r, g, b))
    print "\n"
    client.put_pixels(pixels, channel=0)
    start_pixel += 1
    time.sleep(1/fps)

start_pixel = -pulse_width

#### RED ######################

for run in range( int(n_pixels + pulse_width) ):
    pixels = []
    for current_pixel in range(int(n_pixels)):
        if( (current_pixel >= start_pixel) and (current_pixel < start_pixel + pulse_width) ):
            r         = int(256*(math.sin(math.radians( start_pixel +
                                                        pulse_width -
                                                        current_pixel )/ increment_val)))
            g = b = 0
        else:
            r = g = b = 0
        print r
        pixels.append((r, g, b))
    print "\n"
    client.put_pixels(pixels, channel=0)
    start_pixel += 1
    time.sleep(1/fps)

start_pixel = -pulse_width

#### GREEN ####################

for run in range( int(n_pixels + pulse_width) ):
    pixels = []
    for current_pixel in range(int(n_pixels)):
        if( (current_pixel >= start_pixel) and (current_pixel < start_pixel + pulse_width) ):
            g =         int(256*(math.sin(math.radians( start_pixel +
                                                        pulse_width -
                                                        current_pixel )/ increment_val)))
            r = b = 0
        else:
            r = g = b = 0
        print r
        pixels.append((r, g, b))
    print "\n"
    client.put_pixels(pixels, channel=0)
    start_pixel += 1
    time.sleep(1/fps)

start_pixel = -pulse_width

#### BLUE #####################

for run in range( int(n_pixels + pulse_width) ):
    pixels = []
    for current_pixel in range(int(n_pixels)):
        if( (current_pixel >= start_pixel) and (current_pixel < start_pixel + pulse_width) ):
            b         = int(256*(math.sin(math.radians( start_pixel +
                                                        pulse_width -
                                                        current_pixel )/ increment_val)))
            r = g = 0
        else:
            r = g = b = 0
        print r
        pixels.append((r, g, b))
    print "\n"
    client.put_pixels(pixels, channel=0)
    start_pixel += 1
    time.sleep(1/fps)
