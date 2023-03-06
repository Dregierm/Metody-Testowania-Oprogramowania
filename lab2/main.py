#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    format_str_len = len(format_string)
    while i < format_str_len:    
        if i+1 < format_str_len and format_string[i] == '#' and format_string[i+1] == 'k':
            print(param.swapcase(), end="")
            i += 1  
        else:
                print(format_string[i], end="")
        i += 1    
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

