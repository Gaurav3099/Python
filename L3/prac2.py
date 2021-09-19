#WAPP to count letters digits and other charecters
str = input('enter a string')
lc,dc,oc=0,0,0
for i in range(len(str)):
	if str[i].isalpha():
		lc = lc+1
	elif str[i].isdigit():
		dc = dc+1
	else:
		oc=oc+1
print("Letter count",lc,"Digit count:",dc,"other count",oc )