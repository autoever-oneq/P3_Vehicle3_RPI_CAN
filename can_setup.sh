#!/bin/bash

# can_setup.sh
sudo ip link set can0 up type can bitrate 500000

if [ $? -eq 0 ]; then
    echo "can0 setup success"
    ip link show can0
else
    echo "can0 setup fail"
    exit 1
fi