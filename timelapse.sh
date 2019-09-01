#!/bin/bash

/usr/bin/raspistill -fli 60hz -q 90 -e jpg -dt -ex auto -o /mnt/drivepool/Raspberry\ Pi/basil_timelapse_%08d.jpg
