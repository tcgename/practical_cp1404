import random
number = random.randint (0,100)
in_file = open("results.txt","r")
if number >= 0 and number < 35:
    print("{} is Bad".format(number))
if number >= 35 and number <75:
    print("{} is Passable".format(number))
if number >= 75 and number <100:
    print("{} is Excellent".format(number))
in_file.close()


