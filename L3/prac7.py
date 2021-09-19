#sum of digits given by user
def sod(num):
	sum=0
	while num > 0:
		digit=num%10
		sum=sum+digit
		num=num//10
	return sum
n=int(input("enter a number "))
ans=sod(n)
print("sum=",ans)

