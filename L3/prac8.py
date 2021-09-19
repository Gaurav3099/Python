#sum of digits in number using recursivly
def sod(num):
	if num == 0:
		return 0
	else:
		return (num%10)+sod(num//10)
n=int(input("enter a number"))
num=sod(n)
print("sum=",num)