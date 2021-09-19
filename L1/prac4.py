#swapping without temp

x=int(input("enter first number "))
y=int(input("enter second number "))
print("before swapping " ,x,y)
x=x+y
y=x-y
x=x-y
print("after swapping ",x,y)
n1,n2=n2,n1
print(n1,n2)