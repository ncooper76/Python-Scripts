#Calculates the median, or middle value, of a list of numbers
#The median is the middle value for an odd numbered list, so median of 1,2,3,4,5
# is 3, and the average of the two center values of an even numbered list
#median of 1,2,3,4 is (2+3)/2 = 2.5
def median(numbers):
    med = 0.0
    numbers = sorted(numbers)
    if len(numbers)%2 == 0:
        index1 = int(len(numbers)/2)
        index2 = index1 - 1
        med = (numbers[index1]+numbers[index2])/2.0
    else:
        index = int((len(numbers)/2.0)-0.5)
        med = numbers[index]
    return med
median([3,1,4,5,6,2])
