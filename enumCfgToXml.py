import os
from xml.dom import minidom
from xml.etree import ElementTree as ET

# PROCESS TO CREATE XML FILE; PREPARING TO STORE ALL ENUM INTO XMLxml
enumXml = minidom.Document()
root = enumXml.createElement('root')
enumXml.appendChild(root)
#create MODULE under root
module = enumXml.createElement('module')
module.setAttribute('name','name_of_module')
root.appendChild(module)

#create trace file LOCATION under MODULE
location = enumXml.createElement('location')
location.setAttribute('dir','abs_path_location')
module.appendChild(location)
#create HEADER FILE under MODULE
header_file = enumXml.createElement('header_file')
header_file.setAttribute('name','name_of_header_file')
module.appendChild(header_file)
#create ARRAY under HEADER_FILE
array = enumXml.createElement('array')
array.setAttribute('enum_name','name_of_enum')
header_file.appendChild(array)
#create MEMBER, VALUE under ARRAY
member = enumXml.createElement('member')
member.setAttribute('enum_member','name_of_enum_member')
array.appendChild(member)
enum_value = enumXml.createTextNode('enum_value')
member.appendChild(enum_value)
member.getAttributeNodeNS



enumXmlByteObj = enumXml.toprettyxml(indent='\t', encoding="utf-8")
enumXmlAbsPath = str(os.getcwd()) + "/traceCfg.xml"

with open(enumXmlAbsPath, 'wb') as f:
    f.write(enumXmlByteObj)
f.close()

