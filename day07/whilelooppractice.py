count = 1

while count <= 5:
    num = int(input("Pick a number! "))
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
    count += 1