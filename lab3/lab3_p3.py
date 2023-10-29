# author : Seung Min Lee
# since : 2023-03-25
# purpose : get six random numbers
import random # for randrange number

numbers = []

for i in range(0, 6): # get random number six times
    numbers.append(str(random.randrange(1, 46))) 
    # append stringified number in list
    # integer interval [1, 45]
    
print("Lotto numbers of the week: {}".format(" ".join(numbers))) # add blank between two numbers. 
