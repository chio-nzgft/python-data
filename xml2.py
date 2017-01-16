import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location: ")
print "Retrieving:",url
html = urllib.urlopen(url).read()
stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
print 'count:', len(lst)
s=0

for item in lst:
    s=s+int(item.find('count').text)
print "Sum:", s
