class PartyAnimal:
    x=0
    name=""
    def __init__(self,nam):
        self.name=nam
        print self.name,"constructed"
    def party(self):
        self.x=self.x+1
        print self.name,"party count",self.x
    def party2(self):
        self.x=self.x+2
        print self.name,"party count",self.x
class FootballFan(PartyAnimal):
    points =0
    x=10
    def touchdown(self):
        self.points=self.points+7
        self.party()
        print self.name,"points",self.points
    def party2(self):
        self.x=self.x+100
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
print type(PartyAnimal)
s.x=0
print "============ Sally party2 start =================="
s.party2()
print "============ Sally party2 end =================="
r = FootballFan("Rub")
r.party()
r.touchdown()
r.touchdown()
r.x=0
print "============ Rub party2 start =================="
r.party2()
print "============ Rub party2 end =================="
print type(FootballFan)
print type(r)
print type(r.party)
print type(r.touchdown)
print type(r.name)
'''
Inheritance 繼承
new class (child) 有些 class(parent) 功能
像是 擴展(extends) 的 class 一樣
且 child class 可改 parent class 內的函數
例如 x , party2 就是如此

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
<type 'classobj'>
============ Sally party2 start ==================
Sally party count 2
============ Sally party2 end ==================
Rub constructed
Rub party count 11
Rub party count 12
Rub points 7
Rub party count 13
Rub points 14
============ Rub party2 start ==================
Rub party count 100
============ Rub party2 end ==================
<type 'classobj'>
<type 'instance'>
<type 'instancemethod'>
<type 'instancemethod'>
<type 'str'>
'''
