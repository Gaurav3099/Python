#login operation

noa = 1
while noa <= 3:
	print("attempt number",noa)
	un = input("enter username ")
	pw = input("enter password")
	if(un == 'gaurav') and (pw == 'abc123'):
		print("valid login")
		break
	else:
		print("invalid login")
		noa=noa+1
if noa == 4:
	print("account has been locked")