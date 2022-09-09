from taxi import Taxi
def main():

    taxi = Taxi("prius 1", 100, 1.23)

    autual_distance_driven = taxi.drive(40)
    print(f"taxi drove for {autual_distance_driven} km.")

    print(taxi)
    print(f"current fare: ${taxi.get_fare():.2f}")

    taxi.start_fare()
    autual_distance_driven = taxi.drive(60)
    print(f"tried driving 100km, but taxi drove for {autual_distance_driven} km.")

    print(taxi)
    print(f"current fare: ${taxi.get_fare():.2f}")

if __name__ == '__main__':
    main()