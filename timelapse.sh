#!/bin/bash

raspistill -fli -drc med -q 100 -e jpg -t 300000 -tl 60000 -dt -ex auto -o /mnt/drivepool/Raspberry\ Pi/basil_timelapse_%08d.jpg
