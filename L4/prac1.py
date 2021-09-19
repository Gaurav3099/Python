#count occurance of element
data = []
n = int(input("enter  how many elements"))
for i in range(n):
	ele = int(input('enter element'))
	data.append(ele)
search = int(input('enter element to count'))
count = 0
for i in data:
	if search == i:
		count = count + 1
print('count',count) 