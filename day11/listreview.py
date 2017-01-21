my_good_nature = ("nope", "nada", "not here", "what a shame", "ermmmm", "hmmm", "wow", "i'm", "soooo", "baddd") #store several values into one variable


# simple inefficient printing method

print(my_good_nature[0]) #print first value
print(my_good_nature[1]) #print second value
print(my_good_nature[2]) #print third value
print(my_good_nature[3]) #print fourth value
print(my_good_nature[4]) #print fifth value
print(my_good_nature[5]) #print sixth value
print(my_good_nature[6]) #print seventh value
print(my_good_nature[7]) #print eighth value
print(my_good_nature[8]) #print nineth value
print(my_good_nature[9]) #print tenth value

# or use a while loop

i = 0
while i < len(my_good_nature):
    print(my_good_nature[i])
    i += 1

# or use a for loop

for response in my_good_nature:
    print(response)