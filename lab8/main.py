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
    '0': 'o'
}

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))

def my_printf(format_string, param):
    search = re.search("#(\.\d+)?j", format_string)
    if not search:
        return print(format_string)
    
    to_replace = format_string[search.start() : search.end()]
    hex_param = str(tohex(int(param), 32))[2:]
    hex_len = len(hex_param)
    hex_param = list(hex_param)
    print_zeros = 0

    if search.group(1):
        print_zeros = max(int(search.group(1)[1:]) - hex_len, 0)

    for i in range(len(hex_param)):
        if hex_param[i] == '0' or not hex_param[i].isnumeric():
            hex_param[i] = replacer[hex_param[i]]
    hex_param = str(''.join(hex_param))    

    print(format_string.replace(to_replace, print_zeros*'o' + hex_param))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())

