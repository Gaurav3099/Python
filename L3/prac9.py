#find area using fn overloading
def area(a=None, b=None):
	if(a!=None and b!=None):
		ans=a*b
		print('Area of rectangle ',ans)
	elif(a!=None):
		import math
		ans=math.pi*a**2
		print("Area of circle%8.2f"%ans)
choice=int(input("1 area of rectangle, 2 area of circle"))
if choice == 1:
	length=float(input("eneter length"))
	breadth=float(input("enter breadth"))
	area(length,breadth)
elif choice == 2:
	radius=float(input("eneter radius "))
	area(radius)
else:
	print("invalid choice") 