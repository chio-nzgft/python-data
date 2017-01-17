import urllib
handle = urllib.urlopen('https://raw.githubusercontent.com/paulcarroty/Python-Snippets/master/Coursera%20Programming%20for%20Everybody%20(Python)/mbox-short.txt')
counts=dict()
lst=list()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        z=line.split()[-2:-1][0]
        counts[z[0:2]]=counts.get(z[0:2],0)+1
for k,v in counts.items():
    lst.append((k,v)) 
lst.sort()
for  k,v in lst:
    print (k,v)
