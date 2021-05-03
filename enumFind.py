import re
import os

# PROCESS TO PARSING HEADER FILE

def comment_remover(text):
    '''Remove all kind of commenting from input text'''
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def find_enum(header_file_path):
    '''Parsing enum value from the input HeaderFile'''
    headerFile = open(header_file_path,'r')
    enumFound = re.findall(r"enum\s*(\w+)?\s*{\s*([^}]*)}\s*(\w+)?\s*;", headerFile.read())
    enumDict = {}

    for element in enumFound:
        tempList = list(element)
        enumName = tempList.pop(0)
        if not enumName:
            enumName = tempList.pop(1) # pop(1) instead of pop(2) because index already shift 1 when pop(0) above
        tempList[0] = comment_remover(tempList[0])
        valueList = tempList[0].split(r',')
        enumDict[enumName] = []
        for idx, listValue in enumerate(valueList):
            value = re.findall(r"(\w+_*)+", listValue)
            try:
                if any(x.isalpha() for x in value[1]):
                    value[1] = int(value[1],16)
            except:
                pass
            if idx == 0 and len(value) == 1:
                value.append(r"0")
            elif idx != 0 and len(value) == 1:
                previousValue1 = int(enumDict[enumName][idx-1][1])
                value.append(str(previousValue1 + 1))
            elif idx != 0 and len(value) > 1:
                value[1] = str(int(value[1]))
            else:
                pass
            if value:
                enumDict[enumName].append(value)
    return enumDict