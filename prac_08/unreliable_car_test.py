from prac_08.unreliable_car import UnreliableCar

def main():
    good_car = UnreliableCar("Thor", 100, 90)
    bad_car = UnreliableCar("Hala", 100, 9)

    for i in range(1, 5):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()


