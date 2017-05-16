# This program is for generating random integer data for use in other programs
import random

# this is the counting number of data points and naming output file
n = int(input("How many data points do you want? "))
name = input("What is the name of the output file? ")

#these set the interger range of the random number draw
min_x = int(input("What is the lower number to be selected? "))
max_x = int(input("What is the upper number to be selected? "))

random_data = open(name, "w")
i  = 0 # loop iteriation
data  = 0
while i < n:
    data =  random.randint(min_x,max_x)
    #print(data)
    random_data.write(str(data) + "\n")
    i += 1

random_data.close()
