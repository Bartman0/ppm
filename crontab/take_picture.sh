#!/bin/sh
raspistill -ex auto -h 300 -w 300 -o /tmp/ppm.tmp.jpg
mv /tmp/ppm.tmp.jpg /tmp/ppm.jpg
