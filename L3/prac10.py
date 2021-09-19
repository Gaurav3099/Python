#WAPP bubble sort in ascending order using list
data=[]
n=int(input("enter  number of elements "))
for i in range(n):
	ele=int(input("enter element ")) 
	data.append(ele)
print(data)
for i in range(n-1):
	for j in range(i+1,n):
		if data[i]>data[j]:
			data[i],data[j]=data[j],data[i]
print(data)