import urllib
from BeautifulSoup import BeautifulSoup

def get_html(url,ps):
    p = 0
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        p=p+1
        if p == ps:
            out_url= tag.get('href', None)
            print "Retrieving:",out_url
            return out_url
p = 1
c = 0
url = raw_input("Enter URL: ")
cs = int(raw_input("Enter count: "))
ps = int(raw_input("Enter position: "))
print "Retrieving:",url
while c < cs:
    url=get_html(url,ps)
    c=c+1
