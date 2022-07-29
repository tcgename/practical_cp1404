MIN_LENGTH = 5
MAX_LENGTH = 15

def main():
    print("Please enter a valid password:")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("     1 or more uppercase characters")
    print("     1 or more lowercase characters")
    print("     1 or more numbers")
    print("     and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|")
    password = input(">>> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input(">>> ")
    print("Your {}-character password is valid: {}".format(len(password),password))

def is_valid_password(password):
    count_upper=0
    count_lower=0
    count_digit=0
    count_special=0
    for char in password:
        pass
    return True

main()