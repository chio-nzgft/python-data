import urllib
handle = urllib.urlopen('https://raw.githubusercontent.com/paulcarroty/Python-Snippets/master/Coursera%20Programming%20for%20Everybody%20(Python)/mbox-short.txt')
#開檔

#設定 dict 也就是x 為字典
x=dict()
#一行一行讀檔
for line in handle:
#剔除 "From: "開頭的那行
#抓出 "From"開頭的那行
    if line.startswith("From") and not line.startswith("From:"):
#切割那行成多個字串
#將切割出的第"1" 個字串放到 y  (pythen 第一個字串是 "0")
        y=line.split()[1]
#如x是新建的就放index 為 0 再加 1
#如x是不是新建的就將 index 的值再加 1
        x[y]=x.get(y,0)+1
#宣告None ...將用於判斷是否第一個
bigC=None
#將 x dict 一個一個讀出成 字串及index
for w,c in x.items():
#判斷 是否是第一個(None)  是就將數值放入
#找出最大的index
    if bigC is None or c>bigC:
        bigC=c
        bigW=w
#印出最大的index 及其字串
print bigW,bigC
