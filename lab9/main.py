#!/usr/bin/env python3

import sys
import re

replacer = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    '3': 'd',
    '4': 'e',
    '5': 'f',
    '6': 'g',
    '7': 'h',
    '8': 'i',
    '9': 'j'
}

def my_printf(format_string, param):
    search = re.search("#(\.\d+)?h", format_string)
    if not search:
        return print(format_string)
    
    to_replace = format_string[search.start() : search.end()]
    param_num = 0
    res = ""

    if search.group(1):
        param_num = int(search.group(1)[1:])

    int_part, float_part = divmod(float(param), 1)
    int_part = str(int(int_part))
    float_part = str(round(float_part, param_num))[2:]
    
    for x in int_part:
    	res += replacer[x]
    res += "."		
    
    for x in float_part:
    	res += str((int(x) + 5) % 10)
    


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())

