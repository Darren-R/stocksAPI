from alpha import AlphaVantage

def main():
    while True:
        print('\n')
        print("1. View closing price to NYSE Stock")
        print("2. Last month activity for a Stock")
        print("3. Track Market")
        print("4. Make Gains")
        print("5. Quit")
        try:
            user_action = int(input("What would you like to do? "))
        except:
            print("Input valid choice")
            continue

        if user_action == 1:
            AlphaVantage.closing_price("yesterday")
        elif user_action == 2:
            AlphaVantage.closing_price("last_month")
        elif user_action == 3:
            print("TODO Market graph")
        elif user_action == 4:
            print("BUY LUNA WEN LAMBO")
        elif user_action == 5:
            quit()
        else:
            print("Input valid choice")

if __name__ == "__main__":
    main()