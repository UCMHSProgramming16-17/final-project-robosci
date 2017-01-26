import string
import pandas as pd
from bokeh.charts import save, output_file


# open file, create string
a = 'youth.txt'
b = '1984.txt'
c = 'alice.txt'
d = 'gatsby.txt'
e = 'hamlet.txt'
f = 'huckfinn.txt', 
g = 'mobydick.txt', 
h = 'odyssey.txt'
i = 'warandpeice.txt'
j = 'donquixote.txt'
k = 'prideandprejudice.txt'

filenames = [a, b, c, d, e, f, g, h, i, j, k]

'''
fillin = []
x = 0

for item in filenames:
    fillin.append(open(item, 'r'))
    x += 1
    
print(fillin)
'''
f=[]
def file(name):    
    read_time = open(name, 'r')
    raw_string = read_time.read()
    new_string = raw_string.lower()
    f.append(new_string)

file(str(filenames))

print(f)


cleaned_string = ''

for char in f:
#  add only the characters we want to our cleaned string
    if char in string.ascii_letters:
#         print(char)
        cleaned_string += char + ' '
    elif char in string.whitespace:
#         print(' ')
        cleaned_string += ' '

letters = cleaned_string.split(' ')