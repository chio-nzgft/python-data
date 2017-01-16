# -*- coding: big5 -*-
import win32com.client
import time
global A
A=["十","一","二","三","四","五","六","七","八","九"]
speaker = win32com.client.Dispatch("SAPI.SpVoice") #連接SAPI
SVSFDefault = 0
SVSFlagsAsync = 1
speaker.Volume = 100
speaker.Rate = 1

def ssp(w):
    speaker.Speak(w)
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
        time.sleep(1)
