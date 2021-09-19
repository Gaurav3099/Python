#WAPP sum of digits of given number
num = input("enter a number ")
n = int(num)
sum = 0
while n>0:
	digit = n % 10
	sum = sum + digit
	n = n // 10
else:
	print("Sum =",sum)
	