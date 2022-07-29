def main():
    sales = float(input("Enter sales: $"))
    total = ""
    while sales>=0:
        if sales < 1000:
            total = sales * 0.1
        if sales >= 1000:
            total = sales * 0.15
        print(f"your bonus is {total}")
        sales = float(input("Enter sales: $"))

main()
