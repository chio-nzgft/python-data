'''
Python 物件 class( 類別) , 例如  PartyAnimal

建立了class 件叫 instance(實例) , 如 s, j

instance 中的def(函數) 叫  instancemethod,   如  s.__init__  ,s.party

instance 中的常數 (srt ,int ,list .....) 還是一樣是 instance.srt 或 instance.int 如 s.x , s.name

所以 class 不是實體 , 需實體化  , 例如  s=PartyAnimal("Jim") , 其中 "Jim" 是傳給 __init__ 用的初始參數(不是傳到 self , 是傳到 nam) ,

然而 所有  instance 中的def(函數) , 第一個變數是 self(就是,instance本身)   , 第二個才是 instance 傳進去的參數如 "Jim"

-----------------------------------------------------------------------------------
'''
class PartyAnimal:
    x=0
    name=""
    def __init__(self,nam):
        self.name=nam
        print self.name,"constructed"
    def party(self):
        self.x=self.x+1
        print self.name,"party count",self.x
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()
print type(s)
print type(s.party)
print type(j.__init__)
print type(s.name)
print type(s.x)
print "PartyAnimal for S & x ==> ",s.name,s.x

'''
-----------------------------------------------------------------------------------

Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Sally party count 2
<type 'instance'>
<type 'instancemethod'>
<type 'instancemethod'>
<type 'str'>
<type 'int'>
PartyAnimal for S & x ==>  Sally 2
'''
