#!/usr/bin/env python3

import sys
import re

replacer = {
    'a': 'g',
    'b': 'h',
    'c': 'i',
    'd': 'j',
    'e': 'k',
    'f': 'l',
}

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))

def my_printf(format_string, param):
    search = re.search("#j", format_string)
    if not search:
        return print(format_string)
    
    to_replace = format_string[search.start() : search.end()]
    hex_param = list(str(tohex(int(param), 32))[2:])

    for i in range(len(hex_param)):
        if not hex_param[i].isnumeric():
            hex_param[i] = replacer[hex_param[i]]
    hex_param = str(''.join(hex_param))    

    print(format_string.replace(to_replace, hex_param))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
