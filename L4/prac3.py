#wapp for billing generation
item = {'upma':20,'idli':30,'dosa':20}
for i in item.keys():
	print(i)
amount = 0
while True:
	choice = int(input("1 item 2 exit"))
	if choice == 1:
		i = input("enter the name of item ")
		q = int(input('enter quantity '))
		am = item.get(i,0)*q
		amount=amount+am
	elif choice == 2:
		break
	else:
		print("invalid choice ")
print(amount)