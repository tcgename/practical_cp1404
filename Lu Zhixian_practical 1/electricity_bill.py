def main():

    print("Electricity bill estimator")
    cents_per_kWh = float(input("Enter cents per kWh: "))
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    total = cents_per_kWh * 0.01 * daily_use * billing_days
    print(f"Estimated bill: {total:2f} $")

main()

