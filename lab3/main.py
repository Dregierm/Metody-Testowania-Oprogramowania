#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search = re.search("#(\d+)?(\.\d+)?k", format_string)
    if not search:
        return print(format_string)

    param_len = len(param)
    param_print_len = param_len
    print_spaces = 0
    if search.group(2): #.X
        param_print_len = min(int(search.group(2)[1:]), param_len)

    if search.group(1):
        print_spaces = max(int(search.group(1)) - param_print_len, 0)        

    to_replace = format_string[search.start() : search.end()]
    print(format_string.replace(to_replace, " "*print_spaces + param.swapcase()[:param_print_len]))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
