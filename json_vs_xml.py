print ' Json info ------------------------------'
import json
input1 = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''
 
info1 = json.loads(input1)
print 'User count:', len(info1)
  
for item in info1:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']
    


print ' XML info ------------------------------'
import xml.etree.ElementTree as ET
input2 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>''' 
info2 = ET.fromstring(input2).findall('users/user')    
print 'User count:', len(info2)
    
for item in info2:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")
