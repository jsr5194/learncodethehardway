print("Just some test code - exercise doesn't have any")



def fibGen():
	curVal = 1
	yield curVal
	secondLastVal = 0
	lastVal = 1
	while True:
		curVal = secondLastVal +  lastVal
		secondLastVal = lastVal
		lastVal = curVal
		yield curVal


count = 0
for fib in fibGen():
	if count == 10:
		break

	print(fib)
	count += 1
