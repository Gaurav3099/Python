#find grade marks >90-A >80-B else c
marks=int(input("Enter marks"))
if marks>90:
	grade='A'
elif marks>80:
	grade='B'
else:
	grade='C'
print('Marks',marks,'Grade',grade) 