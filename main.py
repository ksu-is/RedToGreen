import csv
import os

FILENAME = "trades.csv"

def setup_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ticker", "entry", "exit", "contracts", "pnl", "result"])

def add_trade():
    ticker = input("Enter ticker: ")
    entry_price = float(input("Entry price: "))
    exit_price = float(input("Exit price: "))
    contracts = int(input("Contracts: "))

    pnl = (exit_price - entry_price) * contracts * 100

    if pnl > 0:
        result = "Win"
    elif pnl < 0:
        result = "Loss"
    else:
        result = "Break Even"

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ticker, entry_price, exit_price, contracts, pnl, result])

    print("Trade recorded.")
    print("PnL: $" + str(round(pnl, 2)))

def view_trades():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        print("\nYour Trades:")
        for row in reader:
            print(row)

def main():
    setup_file()

    while True:
        print("\nRed to Green Tracker")
        print("1. Add Trade")
        print("2. View Trades")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_trade()
        elif choice == "2":
            view_trades()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

main()
