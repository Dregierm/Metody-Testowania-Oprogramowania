#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search_k = re.search("#(\d+)?(\.\d+)?k", format_string)
    search_g = re.search("#g", format_string)

    if not search_k and not search_g:
        return print(format_string)

    if search_k:
        param_len = len(param)
        param_print_len = param_len
        print_spaces = 0

        if search_k.group(2): #.X
            param_print_len = min(int(search_k.group(2)[1:]), param_len)

        if search_k.group(1): #Xk
            print_spaces = max(int(search_k.group(1)) - param_print_len, 0)        

        to_replace = format_string[search_k.start() : search_k.end()]
        print(format_string.replace(to_replace, " "*print_spaces + param.swapcase()[:param_print_len]))
    elif search_g:
        to_replace = format_string[search_g.start() : search_g.end()]

        if str(param).isnumeric():
            print(format_string.replace(to_replace, str(param)[::-1]))
        else:
            return print(format_string)  

            

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
