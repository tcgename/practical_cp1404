is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
    except :  # TODO - add the exception you want to catch after except
        print("Cannot be zero!")
    result *= result
print("Valid result is:", result)