#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search = re.search("#b", format_string)
    if not search:
        return print(format_string)
    
    to_replace = format_string[search.start() : search.end()]
    
    num = 0	
    try:
        num = int(param)
    except Exception:
        num = 0	
    
    binary = bin(num)[2:]	
    binary = binary[::-1]
    
    if num == 0:
        result = "0"
    else:
        letters = "abcdefghij"
        result = ""
        i = 0
        for digit in binary:
            if i == 10:
                i = 0
            if digit == "1":
                result += letters[i]
            else:
                result += "0"
            i += 1    
                
    result = result[::-1]
    print(format_string.replace(to_replace, result))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())

