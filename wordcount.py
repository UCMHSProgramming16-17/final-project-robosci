import string
import pandas as pd

# open file, create string
file = open('youth.txt', 'r')
raw_string = file.read()
new_string = raw_string.lower()

cleaned_string = ''

for char in new_string:
#  add only the characters we want to our cleaned string
    if char in string.ascii_letters:
#         print(char)
        cleaned_string += char
    elif char in string.digits:
#         print(char)
        cleaned_string += char
    elif char in string.whitespace:
#         print(' ')
        cleaned_string += ' '

words = cleaned_string.split(' ')

word_count = {}

for word in words:
    if word != '':
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

words = []
count = []

for key, value in word_count.items():
    words.append(key)
    count.append(value)

df = pd.DataFrame({'word': words, 'count': count})