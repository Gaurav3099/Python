#check if number is prime or not
n = int(input("enter a number "))
for i in range(2, n):
	if n % i == 0:
		print("not a prime number")
		break
else:
	print("it is a prime number")