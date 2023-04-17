#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search_g = re.search("#(\.\d+)?g", format_string)

    if not search_g:
        return print(format_string)

    to_replace = format_string[search_g.start() : search_g.end()]
    is_negative = int(param) < 0
    if is_negative:
        param = str(abs(int(param))) 
    param_len = len(str(param))	
    
    if str(param).isnumeric():
            if search_g.group(1): #Xg
                print_zeros = max(int(search_g.group(1)[1:]) - param_len, 0)
                param = list(str(param))
                for i in range(0, param_len):
                    param[i] = str((int(param[i]) * 9 + 1) % 10)
                param = str(''.join(param))
                return print(format_string.replace(to_replace,  "-"*is_negative + "0"*print_zeros + param))    
            else: #g
                return print(format_string.replace(to_replace, str(int(str(param)[::-1]))))
    else:
        return print(format_string)  


            
data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
