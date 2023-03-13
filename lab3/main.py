#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search = re.search("#(\.\d+)?k", format_string)
    if not search:
        return print(format_string)

    param_len = len(param)
    param_print_len = param_len
    if search.group(1): #.X
        param_print_len = min(int(search.group(1)[1:]), param_len)

    to_replace = format_string[search.start() : search.end()]
    print(format_string.replace(to_replace, param.swapcase()[:param_print_len]))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
