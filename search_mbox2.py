handle = open("mbox-short.txt")
lst1=list()
lst2=list()
for line in handle:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        x=line.split()
        y=x[-2:-1]
        z=y[0]
        lst1.append((z[0:2],1))
lst1.sort()
count=0
for k,v in lst1:
    if count>0:
        (kr,vr)=lst2[count-1]
    if count==0 or k != kr:
        count=count+1
        lst2.append((k,v))
        continue
    else:
        lst2[-1]=(k,vr+1)
for k,v in lst2:
    print k,v
