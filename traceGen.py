import os
import re
from enumFind import find_enum
from headerScan import scan_header

def file_name(text):
    name = re.findall(r'\/(\w+)+.h$',text)
    return name

testPath = '/Users/khoahuynh/Documents/Document/Python/TraceGen/cHeader.h'
print(file_name(testPath))
enumDict = find_enum(testPath)


# for key, enumList in enumDict.items():
#     for enum in enumList:
#         print("ARRAY " + key.upper()+"_TRACE_ID = " + enum[1] + " : " + enum[0])
#     print("\n")