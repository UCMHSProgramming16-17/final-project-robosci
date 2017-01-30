import string
import pandas as pd
from bokeh.plotting import figure, save, output_file


def counttext(file_name):
    file = open(file_name, 'r')
    raw_string=file.read()
    new_string=raw_string.lower()
    cleaned_string=''
    
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
    
    return letter_count

a = counttext('1984.txt')
b = counttext('alice.txt')
c = counttext('donquixote.txt')
d = counttext('gatsby.txt')
e = counttext('hamlet.txt')
f = counttext('mobydick.txt')
g = counttext('odyssey.txt')
h = counttext('prideandprejudice.txt')
i = counttext('warandpeice.txt')
j = counttext('youth.txt')

letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w','g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']

def process_data(n):
    y = []
    for x in letters:
        y.append(n[x])
    return y

p = figure(x_range=letters, title="Frequency of letters in books", plot_width=1080, plot_height=720)


p.circle(letters, process_data(a), legend="1984", color='blue', size = 10)
p.circle(letters, process_data(b), legend="Alice in Wonderland", color='red', size = 10)
p.circle(letters, process_data(c), legend="Don Quixote", color='green', size = 10)
p.circle(letters, process_data(d), legend="The Great Gatbsy", color='yellow', size = 10)
p.circle(letters, process_data(e), legend="Hamlet", color='violet', size = 10)
p.circle(letters, process_data(f), legend="Moby Dick", color='pink', size = 10)
p.circle(letters, process_data(g), legend="The Odyssey", color='maroon', size = 10)
p.circle(letters, process_data(h), legend="Pride and Prejudice", color='black', size = 10)
p.circle(letters, process_data(i), legend="War and Peace", color='navy', size = 10)
p.circle(letters, process_data(j), legend="Youth", color='salmon', size = 10)

output_file = "plot.html"
save(p)

'''

df = pd.DataFrame({'Letters':letters,
                    '1984': [a[n] for n in letters],
                    'Alice in Wonderland': [b[n] for n in letters],
                    'Don Quixote': [c[n] for n in letters],
                    'The Great Gatsby': [d[n] for n in letters],
                    'Hamlet': [e[n] for n in letters],
                    'Moby Dick': [f[n] for n in letters],
                    'The Odyssey': [g[n] for n in letters],
                    'Pride and Prejudice': [h[n] for n in letters],
                    'War And Peace': [i[n] for n in letters],
                    'Youth': [j[n] for n in letters]
})


def process_data(n):
    y = []
    for x in letters:
        y.append(n[x])
    return y

p = figure(x_range=letters)


p.circle(letters, process_data(a), color='blue', size=20, alpha=.5)

output_file = 'scatterplot.html'

save(p)
'''