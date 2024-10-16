#!/usr/bin/env bash

venv/bin/python3 -m application --debug examples/arp/arp.asm \
    -i examples/arp/arp_in.pcap \
    -o examples/arp/arp_out \
    -t examples/arp/arp_tables.json
