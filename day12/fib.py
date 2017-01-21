# ask for input regarding fibbonacci length
count = int(input("enter the # of fibbonacci nums you want to calculate after 1,1"))

# starting point of fib sequence
fiblist = [1,1]

# take fiblist and add length under variable temp
for x in range (count):
    temp = fiblist[-1] + fiblist[-2]
    fiblist.append(temp)

# print final sequence
print(fiblist)