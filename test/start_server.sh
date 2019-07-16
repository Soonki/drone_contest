#!/bin/sh

/usr/local/bin/mjpg_streamer -i "input_raspicam.so -x 640 -y 480 -fps 15 -q 80" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www" -b
