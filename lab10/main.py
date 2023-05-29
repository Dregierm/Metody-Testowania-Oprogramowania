#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search = re.search("#a", format_string)
    if not search:
        return print(format_string)
    
    to_replace = format_string[search.start() : search.end()]
    
    param_num = 0	
    res = 0
    try:
    	param_num = int(param)
    	param_n = len(str(param_num))
    	res = int( (param_num * 2 ) / param_n )
    except Exception:
    	param_num = 0	
    
    if res % 2 != 0:
    	res = hex(res)[2:]
	
    res = str(res)		
    
    print(format_string.replace(to_replace, res))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())

