numbers = []
for i in range(1,6):
    number = input("Number: ")
    numbers.append(number)
total = 0
for i in range(1,6):
    number = numbers[i - 1]
    total += number[i-1]
average = total/5
print(numbers[0])
print(numbers[4])
print(min(numbers))
print(max(numbers))
print(average)


