#Factorial of number
n = int(input("enter a number "))
f = 1
if (n < 0):
	print("number is negative")
elif (n == 0):
	print("factorial=",1)
else:
	for i in range(1,n+1):
		f = f * i
	print("factorial =",f)