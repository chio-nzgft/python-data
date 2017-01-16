import sl4a
import time
global A
A=["十","一","二","三","四","五","六","七","八","九"]

droid=sl4a.Android()
def ssp(w):
    droid.ttsSpeak(w)
    print (w)
def sp(i):
    if i<10:
        ssp(A[i])
    else:
        k=i//10
        if k>1:
            sp(k)
        ssp(A[0])
        s=i%10
        if s > 0:
            sp(s)
        
for x in range(2,10):
    for y in range(1,10):
        sp(x)
        sp(y)
        sp((x*y))
        print (" ")
        time.sleep(2)
