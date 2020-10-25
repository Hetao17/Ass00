# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

first_name='hetao'
last_name='ren'

# E1.1 
### Start of your code ##
First_name=str.capitalize(first_name)
Last_name=str.capitalize(last_name)
### End   of your code ##
print(First_name)
print(Last_name)

# E1.2
### Start of your code ##
name=' '.join([first_name, last_name])
### End   of your code ##
print(name)

# E1.3
### Start of your code ##
NAME=str.upper(name)
### End   of your code ##
print(NAME)

# E1.4
### Start of your code ##
FIRST_NAME=str.upper(first_name)
LAST_NAME=str.upper(last_name)
NAME_count=len(''.join([FIRST_NAME, LAST_NAME]))
print(NAME,'has',NAME_count,'letters')
Spell=list(''.join([FIRST_NAME, LAST_NAME]))
print(Spell)
occurrences=NAME_count
selected_character="I"
### End   of your code ##
print('%d  %s in:  %s '%((0 if occurrences==-1 else occurrences), selected_character,NAME))
print("The first letter of your name is {}.".format(NAME[0])) # str.format
print(f"The last letter of your name is {NAME[-1]}.")
TUBS_email = 'tu-bs.de'
print(f"\n{First_name[0]}.{Last_name}@{TUBS_email} could be a proper email-address for you.")

# E1.5
Scientific={'Numpy','Scipy'}
Editors = set(['Spyder','vsCode'])
Visualization=set()
Visualization.add('Gluviz')
Visualization.update(['Matplotlib'])
print(f"Visualization is now:{Visualization}")
### Start of your code ##
check_seaborn='seaborn' in Visualization
print(check_seaborn)

print(f"seaborn was {'not' if check_seaborn == False else '' } in the Visualization list.")
if check_seaborn == False:
    Visualization.update(['seaborn'])
### End   of your code ##
print(f"Visualization is now:{Visualization}")

# E1.6
### Start of your code ##
tools=Visualization.union(Scientific,Editors)
print(tools)
Browser_based = set(['Jupyterlab','Jupyter Notebook','Colab','pandas'])
### End   of your code ##
print(f"Browser_based set is now:{Browser_based}")

# E1.7
Browser_based.remove('pandas')
print(f"Browser_based set is now:{Browser_based}")
tools=tools.union(Browser_based)
print(f"tools set is updated to:{tools}")

# E1.8
import random
random.seed(57)
B = [random.randint(0,10) for i in range(20)]
print(f'B={B}')
count = {}
for item in B:
      count[item] = B.count(item)
print(count)
most_frequent = max(B,key=B.count)
print(f'most_frequent number is = {most_frequent}')

# E1.9
random.seed(57)
C = [random.randint(0,10) for i in range(20)]
dict = {}
for key in C:
    dict[key] = dict.get(key, 0) + 1
print(dict)

random.seed(57)
C = [random.randint(0,10) for i in range(20)]
print(sorted(C))
count = {}
for item in C:
      count[item] = C.count(item)
count_C=count
print(count_C)

# E1.10
import numpy as np
from sklearn.metrics import accuracy_score
y_true = [1, 2, 0, 1, 1, 2, 3, 1, 2, 1]
y_pred = [1, 2, 1, 1, 1, 0, 3, 1, 2, 1]


correct = 0
total_elements = 0
print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize=False))

# E1.11
random.seed(57)
B = [random.randint(0,10) for i in range(25)]
print(f'B={B}')

### Start of your code ##
dict = {}
for key in B:
    dict[key] = dict.get(key, 0) + 1
print(dict)
B_and_freq=dict
### End   of your code ##

print(f'B and frequencies ={B_and_freq}')

# E1.12
### Start of your code ##
most_frequent = max(B,key=B.count)
occurrences=dict[max(B,key=B.count)]
### End   of your code ##

print(f'most_frequent number is {most_frequent} which is repeated {occurrences} times')

















