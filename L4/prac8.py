class Employee:
	def __init__(self,name,per_day_salary):
		self.name=name
		self.per_day_salary=per_day_salary
	def __mul__(self,other):
		return self.per_day_salary*other.no_of_days_worked
class Attendance:
	def __init__(self,no_of_days_worked):
		self.no_of_days_worked=no_of_days_worked
e=Employee("Amit",120)
a=Attendance(24)
salary=e*a
print("Salary",salary)