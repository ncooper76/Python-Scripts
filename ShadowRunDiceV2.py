# This script rolls dice for the RPG Shadowrun, the roll technique is you roll
# N number of 6 sided dice against a target number. For every die that equals or excedes
# The target number you get a success. 0 successes means that you fail the task.
# If you roll all ones it is a critical failure
# 1 or 2 successes means you barely succeeded
# 3 or 4 means that you did okay
# 5 or more successes means you aced it.

#Pyplot for Data Visualizations
import matplotlib.pyplot as plt
# Import numpy and set seed
import numpy as np
import time

#set unique RNG seed for rubustness in die rolling
np.random.seed(int(time.time()))

#This list tracks indiviual dice for evaluation against a target number
skill_check = []
success = 0
botch = 0

#To assign the number of dice to throw, always an interger >0
dice_pool = int(input("How many dice do you need to throw for the success test? "))

#To assign a target number to roll against
tn = int(input("What is the target number of this success test? "))


#6's in SR are open-ended. If you roll a 6 you reroll that die and add the result
#You repeat until the die is not a 6. This allows Target numbers to excede 6
for i in range(dice_pool):
    dice = np.random.randint(1,7)
    roll = dice
    if tn > 6: #open ended die rolling only needed if target number excededs 6
        while dice == 6:
            dice = np.random.randint(1,7)
            roll = roll + dice
    skill_check.append(roll)
#print(skill_check)

#This counts for successes and botches, if botches = die pool its a critical failure
for die in skill_check:
    if(die >= tn):
        success += 1
    elif(die == 1):
        botch += 1

if(botch == dice_pool):
    print("You done messed up A-A-Ron!")
    
print("You rolled " + str(success) + " successes.")

#Gives a graphical display of your success test
plt.hist(skill_check, bins =max(skill_check))
plt.show()
