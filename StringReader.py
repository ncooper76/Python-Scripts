#This is a test script to pass a csv file of text into a python list.

import csv

with open('C:\\Users\\Nate\\Documents\\DataSet\\A_advice.csv', 'r') as a:
    reader = csv.reader(a)
    A_advice = list(reader)

for block in A_advice:
    for line in block:
        print(block.index(line), line)
choice = int(input("Input the number that best fits the student for "))
print(A_advice[0][choice])
'''
with open('C:\\Users\\Nate\\Documents\\DataSet\\B_advice.csv', 'r') as b:
    reader = csv.reader(b)
    B_advice = list(reader)

for block in B_advice:
    for line in block:
        print(block.index(line), line)

with open('C:\\Users\\Nate\\Documents\\DataSet\\C_advice.csv', 'r') as c:
    reader = csv.reader(c)
    C_advice = list(reader)
    
for block in C_advice:
    for line in block:
        print(block.index(line), line)

with open('C:\\Users\\Nate\\Documents\\DataSet\\F_advice.csv', 'r') as f:
    reader = csv.reader(f)
    F_advice = list(reader)

for block in F_advice:
    for line in block:
        print(block.index(line), line)
'''
a.close()
#b.close()
#c.close()
#f.close()
