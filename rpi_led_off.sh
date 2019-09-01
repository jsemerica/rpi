#!/bin/bash
echo 0 | sudo tee /sys/class/leds/led1/brightness
echo gpio | sudo tee /sys/class/leds/led1/trigger
