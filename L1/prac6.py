#check leap year
year=int(input('enter a year '))
if ((year%400 == 0) or (year %4 == 0 and year %100 !=0)):
	print("its a leap year ")
else:
	print("not a leap year")