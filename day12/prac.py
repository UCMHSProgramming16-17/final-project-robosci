animals = [cat, dog, otter, squid, snake]

animals[4] #prints snake, and is simple. however there is not adaption for last term

animals[len(list)-1] #adapts and not as simple

animals[-1] # same adaption as the 5th line, but simple like 3rd line


#Now, with the lesson learned, here's how to do the fibbonnaci sequence correctly:
#want to get seq = [1,1] to [1,1,2,3,4,8,13,21,34,55]. The idea is to take the 2 previous numebers and add to the next one

# One way:
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
    
# Another way:
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
for index, fibonacci_number in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
     if index == 10:
         break

#Yet another way:
def fibb(n):
    if n < 2:
        return n
    return fibb(n-2) + fibb(n-1)
    
#but that seems alittle hard so the class way to do it is

sequence = [1, 1] #create a list

new_val = sequence[-1] + sequence[-2] #figure out next value
print("Sequence starts out with", sequence)

desired_length = input("Choose how many numbers in fibb sequence.")
while len(sequence) < desired_length:
    sequence.append(new_val) # add next value to list
    print("New value is ", new_val)
    sequence.append(new_val) #add next value to list
    print("Adding", new_val, "to sequence")
    print("sequence is now", sequence)

#using a for loop:

count = 1
for num in sequence:
    print(str(count) + "-", num)
    count += 1