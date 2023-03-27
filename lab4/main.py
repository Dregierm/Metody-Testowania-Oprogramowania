#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search_g = re.search("#g", format_string)

    if not search_g:
        return print(format_string)

    if search_g:
        to_replace = format_string[search_g.start() : search_g.end()]

        if str(param).isnumeric():
            print(format_string.replace(to_replace, str(int(str(param)[::-1]))))
        else:
            return print(format_string)  

            
data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
