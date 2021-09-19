#WAPP to find wheather input is letter or digit or some other charecter

str = input("enter a charecter ")
ch = str[0]
if ch.isalpha():
	print("it is a letter ")
elif ch.isdigit():
	print("it is a digit")
else:
	print("it is some other charecter ")