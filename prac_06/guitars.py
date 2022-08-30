from prac_06.guitar import Guitar

def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Line 6 JTV-59", 2010, 1512.90)
    guitar_3 = Guitar("Fender Stratocaster", 2014, 765.40)
    print("My guitars!")
    print(F"Name: {guitar_1.name}\nYear: {guitar_1.year}\nCost: {guitar_1.cost}")
    print("{} added.".format(guitar_1))
    print(F"\nName: {guitar_2.name}\nYear: {guitar_2.year}\nCost: {guitar_2.cost}")
    print("{} added.".format(guitar_2))
    print(F"\nName: {guitar_3.name}\nYear: {guitar_3.year}\nCost: {guitar_3.cost}")
    print("{} added.".format(guitar_3))
    print("\n\n... snip ...\n\n")
    print("These are my guitars:")
    for i in range (1,3):
        print()





if __name__ == '__main__':
    main()