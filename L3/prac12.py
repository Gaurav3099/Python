#implement STACK/LIFO using LIST
stack=[]
while True:
	choice=int(input("1 push, 2 pop, 3 peek, 4 display, 5 exit "))
	if choice == 1:
		ele=int(input("enter element to push "))
		stack.append(ele)
	elif choice == 2:
		if len(stack)>0:
			pele=stack.pop()
			print("poped elemnt ",pele)
		else:
			print("stack is empty")
	elif choice == 3:
		if len(stack)>0:
			tele=stack[len(stack)-1]
			print("topmost elemnt ",tele)
		else:
			print("stack is empty")
	elif choice == 4:
		for i in stack:
			print(i,end='')
		print()
	elif choice == 5:
		break
	else:
		print("invalid choice")
