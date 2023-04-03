#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search_g = re.search("#(\d+)?g", format_string)

    if not search_g:
        return print(format_string)

    to_replace = format_string[search_g.start() : search_g.end()]
    param_len = len(str(param))
    is_min = 1 if str(param)[0] == '-' else 0		
    if str(param).isnumeric() or is_min:
            if search_g.group(1): #Xg
                print_spaces = max(int(search_g.group(1)) - param_len, 0)
                param = list(str(param))
                for i in range(is_min, param_len):
                    param[i] = str(int(param[i]) - 1) if param[i] != '0' else '9'
                param = str(''.join(param))
                return print(format_string.replace(to_replace,  " "*print_spaces + param))    
            else: #g
                print(format_string.replace(to_replace, str(int(str(param)[::-1]))))
    else:
        return print(format_string)  


            
data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
