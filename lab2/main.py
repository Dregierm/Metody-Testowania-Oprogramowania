#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    format_str_len = len(format_string)
    num_len = 0
    while i < format_str_len:    
        if i+1 < format_str_len and format_string[i] == '#' and format_string[i+1] == 'k':
            print(param.swapcase(), end="")
            i += 1  
        elif i+3 < format_str_len and format_string[i] == '#' and format_string[i+1] == '.':
            i += 2
            while format_string[i].isdigit():
                num_len += 1
                i += 1
            if num_len == 0:
                print(format_string[i-2:i+1], end="")
            elif format_string[i] != 'k':
                print(format_string[i-num_len-2:i+1], end="")
            else:
                num = int(format_string[i-num_len:i])
                print(param[:num].swapcase(), end="")
                num_len = 0    
        else:
                print(format_string[i], end="")
        i += 1    
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

