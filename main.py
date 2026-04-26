import csv

FILENAME = "trades.csv"

def add_trade():
    ticker = input("Enter ticker: ")
    entry = float(input("Entry price: "))
    exit = float(input("Exit price: "))

    pnl = (exit - entry) * 100

    print("PnL:", pnl)

def main():
    print("Red to Green Tracker")

    choice = input("Press 1 to add trade: ")

    if choice == "1":
        add_trade()

main()
