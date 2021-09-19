#linear search
data=[]
n=int(input("enter number of elements"))
for i in range(n):
	ele=int(input("enter element "))
	data.append(ele)
print(data)
f=int(input("eneter element to find "))
found=False
for i in range(n):
	if data[i] == f:
		print("element found at ",i+1)
		found = True
if found == False:
	print("element not found")
	