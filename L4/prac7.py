class Bee:
	def __init__(self,nop):
		self.nop=nop
	def __add__(self,other):
		ans=self.nop+other.nop
		return ans
	def __sub__(self,other):
		ans=self.nop-other.nop
		return ans
	def __gt__(self,other):
		return self.nop>other.nop
class Mech:
	def __init__(self,nop):
		self.nop=nop
	def __gt__(self,other):
		return self.nop > other.nop
b1=Bee(100)
b2=Mech(200)
r1=b1+b2;	print(r1)
r2=b1+b2;	print(r2)
r3=b1>b2;	print(r3)
r4=b2>b1;	print(r4) 