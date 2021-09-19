class Rbi:
	def __init__(self,num,balance=0.0):
		self.num=num
		self.balance=balance
	def roi(self):
		print('roi is 2 %')
class NayaBank(Rbi):
	def __init__(self,num,balance):
		super().__init__(num,balance)
	def roi(self):
		if self.balance > 10000:
			print("roi is 5%")
		else:
			super().roi()
class Sbot(Rbi):
	def __init__(self,num,balance):
		super().__init__(num,balance)
	def roi(self):
		super().roi()
n=NayaBank(10,50000);	n.roi()
s=Sbot(20,400);		s.roi()