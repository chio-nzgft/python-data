import json
import urllib
print "Sum of count:",sum(x['count'] for x in json.loads(str(urllib.urlopen('http://python-data.dr-chuck.net/comments_349706.json').read()))['comments'])
