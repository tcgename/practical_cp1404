try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1. if you enter decimalnumber or not a number it will be valueerror

#2. if you enter a zero in the denominator it will be zerodivisionerror

#3. can't change

