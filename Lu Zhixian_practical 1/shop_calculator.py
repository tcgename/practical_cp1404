def main():
    number = int(input("Number of items: "))
    set=''
    while set != 0:
        price = float(input("Price of item: "))
        price += price
        set = number
        set -= 1
        if price > 100:
            total = price * 0.9
        else:
            total = price
    print(f'total price for {number} items is {total}')

main()