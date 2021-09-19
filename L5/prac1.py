#WAMDPP to ccheck even odd wwith exception handling
while True:
	try:
		choice = int(input("1 for check 2 exit "))
		if choice == 1:
			num = int(input("enter a number "))
			res=num%2
			if res == 0:
				print("even")
			else:
				print("odd")
		elif choice == 2:
			break
		else:
			print("invalid choice")
	except ValueError:
		print("enter a valid integer")