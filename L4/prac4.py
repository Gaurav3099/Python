import math
class Circle:
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		ans = math.pi*self.radius**2
		print("Area= ",ans)
		print("Area= %7.2f"%ans)
	def circum(self):
		ans=2*math.pi*self.radius
		print("Circumference= ",ans)
		print("Circumference= %f7.2" %ans)
radius = float(input("enter radius of circle "))
c=Circle(radius)
c.area()
c.circum()