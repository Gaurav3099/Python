#find max and min elements
import array
e = array.array("i",[])
n = int(input("enter number of elements "))
for i in range(n):
	d = int(input("enter elements "))
	e.append(d)
max = min = e[0]
for i in range(1, n):
	if e[i] > max:
		max = e[i]
	if e[i] < min:
		min = e[i]
print("max element ",max)
print("min element ",min)