#WAMDPP for file update
import os
while True:
	choice = int(input("1 create a file, 2 delete a file \n 3 read a file 4 write a file \n 5 exit " ))
	if choice == 1:
		fn = input("enter file name to be created ")
		if not os.path.exists(fn):
			f = open(fn,'a')
			print(fn,'created')
			f.close()
		else:
			print("file in use")
	elif choice == 2:
		fn = input("enter file name to be deleted ")
		if os.path.exists(fn):
			os.remove(fn)
			print(fn,'deleted')
			
		else:
			print("file does not exists")
	elif choice == 3:
		fn = input("enter a file name ")
		if os.path.isfile(fn):
			f = open(fn)
			data = f.read()
			print (data)
			f.close()
		else:
			print("file does not exists")
	elif choice == 4:
		fn=input("enter file name to write")
		if os.path.exists(fn):
			f=open(fn,'a')
			data=input("enter data an q to exit \n")
			while data !='q':
				f.write(data + "\n")
				data=input()
			f.close()
		else:
			print("file does not exists")
	elif choice == 5:
		break
	else:
		print("invalid choice")			