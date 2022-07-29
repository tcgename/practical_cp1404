#1
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#2
for i in range (0,110,10):
    print(i, end='  ')
print()

#3
for i in range (20,0,-1):
    print(i, end='  ')
print()

#4
number=int(input("enter a number: "))
for i in range (number):
    print('*', end='')
print()

#5
number = int(input("enter a number: "))
for number in range (number):
    for i in range (number+1):
        print('*', end='')
    print()

