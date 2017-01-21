#practice exercise 1:

def true_false(even):
    if int(even) % 2 == 0:
        return "true"
    else:
        return "false"
        
print(true_false(3))
print(true_false(2))

#practice excercise 2:
def Sum_of_list(a_list):
    return sum(a_list)
    
print(Sum_of_list([5, 4, 7]))
