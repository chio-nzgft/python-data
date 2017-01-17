import urllib
handle = urllib.urlopen('https://raw.githubusercontent.com/chio-nzgft/python-data/master/mbox-short.txt')
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
