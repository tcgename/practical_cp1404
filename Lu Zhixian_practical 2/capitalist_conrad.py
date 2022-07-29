def main():
    import random

    MAX_PRICE = 1000.0
    MIN_PRICE = 0.01
    MAX_DECREASE = 0.05
    MAX_INCREASE = 0.1
    DAY = 0
    starting_price = 10.0
    price = starting_price
    print("Starting price is ${:,.2f}".format(price))

    while price >= MIN_PRICE and price <= MAX_PRICE:
        count = 0
        if random.randint(1, 2) == 1:
            count = random.uniform(-MAX_DECREASE, 0)
        else:
            count = random.uniform(0, MAX_INCREASE)
        price *= (1 + count)
        DAY += 1
        print("On day {} price is: ${:,.2f}".format(DAY, price))

main()
