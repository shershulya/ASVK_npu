#!/usr/bin/env bash

venv/bin/python3 -m application examples/l2sw/l2sw.asm \
    -i examples/l2sw/l2sw_in.pcap \
    -o examples/l2sw/out \
    -t examples/l2sw/l2sw_tables.json
