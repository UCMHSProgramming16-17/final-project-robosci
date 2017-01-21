def in_to_cm(inch):
	cm = inch * 2.54
	return cm

def cm_to_m(cm):
	m = cm / 100
	return m

print(cm_to_m(in_to_cm(int(input("How many inches? ")))))


#and

def another_useless_function():
	print(1)
	print(2)
	print(3)
	return
	print(4)
	print(5)
	
another_useless_function()


def another_useless_function():
	print(1)
	print(2)
	print(3)
	return "john"
	print(4)
	print(5)
	
another_useless_function()


#and 

def fib(qty):
	seq = [1, 1]
	while len(seq) < qty:
		next_val = seq[-1] + seq[-2]
		seq.append(next_val)
	
	for x in seq:
		print(x)

def fib10():
	fib(10)
	
fib10()
fib(13)
