#Wapp to access two class perform n1/n2
import sys
try:
	n1=int(sys.argv[1])
	n2=int(sys.argv[2])
	ans=n1/n2
	print(ans)
except ValueError:
	print("both number should be integer")
except IndexError:
	print("u need to enter 2 integer")
except ZeroDivisionError:
	print("2nd number should not be 0")