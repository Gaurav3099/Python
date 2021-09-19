import pickle
class Student:
	def __init__(self,rno,name):
		self.rno=rno
		self.name=name
	def show(self):
		print('rno',self.rno,'name',self.name)
s=[]
try:
	f=open('student.ser','rb')
	s=pickle.load(f)
	f.close()
except:
	pass
while True:
	choice=int(input("1 add student, 2 remove student,3 view student, 4 exit "))
	if choice == 1:
		rno=int(input("enter roll number "))
		name=input("enter name ")
		st=Student(rno,name)
		s.append(st)
	elif choice== 2:
		pass
	elif choice == 3:
		for i in s:
			i.show()
	elif choice == 4:
		try:
			f=open('student ser','wb')
			pickle.dump(s,f)
			f.close()
		except:
			pass
		break
	else:
		print("invalid choice")