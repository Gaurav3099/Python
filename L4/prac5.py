class Student:
	def __init__(self, rno, p, c, m):
		self.rollno=rno
		self.physics=p
		self.chemistry=c
		self.maths=m
	def avg_of_marks(self):
		sum=0
		sum=self.physics+self.chemistry+self.maths
		avg=sum/3
		print('Average %5.2f'%avg)
s=input("enter roll no, physics, chemistry and maths info")
data=s.split()
rollno=int(data[0])
physics=int(data[1])
chemistry=int(data[2])
maths=int(data[3])
s=Student(rollno, physics, chemistry, maths)
s.avg_of_marks()