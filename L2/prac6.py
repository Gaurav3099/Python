#imlement data structure STACK/LIFO
import array 
st = array.array('i',[])
while True:
	choice = int(input('1 push, 2 pop, 3 peek, 4 display and 5 exit'))
	if choice == 1:
		data = int(input("enter element "))
		st.append(data)
	elif choice == 2:
		if (len(st) > 0):
			pope = st.pop()
			print('element popped',pope)
		else:
			print('Stack is empty')
	elif choice == 3:
		if (len(st) > 0):
			peeke = st[len(st) -1]
			print('topmost element',peeke)
		else:
			print('Stack is empty')
	elif choice == 4:
		for i in st:
			print(i,end ="")
		print()
	elif choice == 5:
		break
	else:
		print("invalid choice")
