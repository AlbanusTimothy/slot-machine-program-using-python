# python slot machine
import random

def spin_row():
    symbols=['🍒','🍉','⭐','🔔', '🍋']

    return [random.choice(symbols) for _ in range(3)]   


def print_row(row):
    print("**********************")
    print(" | ".join(row))
    print("**********************")

def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet *3.5
        elif row[0]=='🍉':
            return bet *4
        elif row[0]=='🍋':
            return bet *5
        elif row[0]=='🔔':
            return bet * 10
        elif row[0]=='⭐':
            return bet *20
    return 0    

        


def main():
    balance = 100

    print("************************")
    print("welcome to python slots ")
    print("symbols: 🍒🍉⭐🔔 🍋")
    print("****************************")


    while balance>0:
        print(f"current balance: ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid number")
            continue


        bet=int(bet)

        if bet > balance:
            print(f"insufficient funds in your wallet to place a bet worth: ${bet} your current balance is: ${balance}")
            continue

        if bet<= 0:
            print(f"bet must be greater than 0, you cant place a bet worth: ${bet}")
            continue

        balance-= bet

        row= spin_row()
        print("spinning....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"you won: ${payout}")
        else:
            print("you lost this round!")

        balance += payout  

        play_again = input("Do you want to spin again asap? (y/n): ").lower()
        if play_again != 'y':
            break    


    print(f"game over your final balance is: ${balance}")    






if __name__=="__main__":
    main()    