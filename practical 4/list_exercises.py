numbers = []
for i in range(1,6):
    number = input("Number: ")
    numbers.append(number)
total = 0
for i in range(1,6):
    number = numbers[i - 1]
    total += number[i-1]
average = total/5
print(f"the first number is {numbers[0]}")
print(f"the last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")


