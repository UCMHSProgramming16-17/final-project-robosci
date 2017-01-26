import string
import pandas as pd
from bokeh.charts import Bar, save, output_file

# open file, create string
file = open('youth.txt', 'r')
raw_string = file.read()
new_string = raw_string.lower()

cleaned_string = ''

for char in new_string:
#  add only the characters we want to our cleaned string
    if char in string.ascii_letters:
#         print(char)
        cleaned_string += char + ' '
    elif char in string.whitespace:
#         print(' ')
        cleaned_string += ' '

letters = cleaned_string.split(' ')

letter_count = {}

for letter in letters:
    if letter != '':
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

letters = []
count = []

for key, value in letter_count.items():
    letters.append(key)
    count.append(value)

df = pd.DataFrame({'letter': letters, 'count': count})

print(df)

chart = Bar(df, label = "letter", values = 'coun', title = "Frequency of Letters", xlabel = "word", ylabel = "count",bar_width=.4)

output_file = 'barchart.html'

save(chart)