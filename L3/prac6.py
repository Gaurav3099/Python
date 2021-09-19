#product using recurssion
def prod(a,b):
	if(a==0 or b==0):
		return 0
	else:
		return a + prod(a,b-1)
n1=int(input("enter first number "))
n2=int(input("enter second number "))
p=prod(n1,n2)
print('answer =',p)