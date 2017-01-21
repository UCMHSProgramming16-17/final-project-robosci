count = int(input("enter the # of loc nums you want to calculate"))

loclist = [2,1]

for x in range (count):
    temp = loclist[-1] + loclist[-2]
    loclist.append(temp)

print(loclist)

