''' This is a program that will test the Monte Hall Paradox
If there are 3 doors, behind one is a new car and behind the other doors
are nothing. After you chose, if one door is opened showing nothing,
Is it better to switch or better to stay? The paradox come when
people say that it is 50-50 because you wind up with two doors
But is that the case? run the script and find out!
'''
import random
import matplotlib.pyplot as plt

doors = ["1", "2", "3"] #The doors to choose from
choice = 0
stay_win = 0
switch_win = 0
stay_lose = 0
switch_lose = 0
play  = 0
'''Stay loop: note that since this is the stay case, if the initial guess wins
elimating a door doesn't make a diference to the outcome; you're not going to change
your mind'''
while(play < 1000):
    prizes = ["Car", "Goat", "Nothing"] #traditional prizes in Let's Make a Deal
    random.shuffle(prizes) #I'm going to shuffle everything to make it as honest as I can
    print(doors)
    choice = random.randint(0,2) #double shuffle between the choice and the prize to keep it honest
    print("I chose door number " + str(choice+1))
    eliminated  = random.randint(0,2) #We have to chose a door to be open
    while(eliminated == choice or prizes[eliminated] == "Car" ):
        eliminated = random.randint(0,2) # roll until the eliminated door is not the choice or the winner
    print("Eliminate door number " + str(eliminated+1))
    print("I stay with " + str(choice+1) + "!")
    if(prizes[choice] == "Car"):
        print("You win a NEW CAR!")
        stay_win += 1
        play += 1
        continue
    else:
        print("You lose! Thanks for playing")
        stay_lose += 1
        play += 1
        continue


'''
This is the loop for the Switch case. Control flow here is tricky becuase you
cannot chose a door that is eliminated and you cannot switch to an eliminated
door. All loops are designed to bare this constraint in mind
'''

play = 0 # reset the play counter
switch = -1 # this will be the choice to switch to later
while(play < 1000):
    prizes = ["Car", "Goat", "Nothing"] #So far same as above, not the duds being different helps the for loop below
    random.shuffle(prizes)
    print(doors)
    choice = random.randint(0,2)
    print("I chose door number " + str(choice+1))
    eliminated  = random.randint(0,2) #We have to chose a door to be open
    while(eliminated == choice or prizes[eliminated] == "Car" ):
        eliminated = random.randint(0,2) # roll until the eliminated door is not the choice or the winner
    print("Eliminate door number " + str(eliminated+1))
    for prize in prizes: #Now we have to pick the door that that was not initially chosen or eliminated
        if(prize != prizes[choice] and prize != prizes[eliminated]):
            switch = prizes.index(prize)
            print("I switch to door number " +str(switch+1))
            break
        else:
            continue
    if(prizes[switch] == "Car"): #tests if your switch choice wins
        print("You win a NEW CAR!")
        switch_win += 1
        play += 1
        continue
    else:
        print("You lose! Thanks for playing")
        switch_lose += 1
        play += 1
        continue
    
labels1 = ['Stay Wins','Stay Loses'] #Pie chart for the Stays
values1 = [stay_win,stay_lose]
explode = (0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(values1, explode=explode, labels=labels1, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

labels2 = ['Switch Wins','Switch Loses'] #Pie chart for the Switches
values2 = [switch_win,switch_lose]
explode = (0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(values2, explode=explode, labels=labels2, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


'''
win_percent1 = stay_win/1000
lose_percent1 = stay_lose/1000
print("Stay win percentage is " + str(win_percent1))
print("Stay lose percentage is " + str(lose_percent1))

win_percent2 = switch_win/1000
lose_percent2 = switch_lose/1000
print("Switch win percentage is " + str(win_percent2))
print("Swtich lose percentage is " + str(lose_percent2))
'''
