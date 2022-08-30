from prac_06.guitar import Guitar

def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Fender Stratocaster", 2014, 765.4)
    print(guitar)
    print(another_guitar)
    print(f"Gibson L-5 CES get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"Fender Stratocaster get_age() - Expected 8. Got {another_guitar.get_age()}")
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"Fender Stratocaster get_age() - Expected True. Got {another_guitar.is_vintage()}")




if __name__ == '__main__':
    main()

