'''from logic import *
add(2,6)
sub(10,6)
mul(4,5)
div(6,3)
'''

from logic import *
acc_num = int(input("Enetr the account number :"))
pin = int(input("Enter the PIN :"))

if logic(acc_num,pin):
    print("Welcome To The ATM")

    while True:
        print("[C]heck Balance")
        print("[D]eposit")
        print("[W]ithdraw")
        print("[V]iew Transcations")
        print("[E]xit)")

        ch = input("Enter the choice: ").upper()
        if ch == "C":
            check_balance()
        elif ch == "D":
            deposit()
        elif ch == "W":
            withdraw()
        elif ch == "V":
            viewtranscation()
        elif ch == "E":
            print("Thank you")
            break
        else:
            print("Enter the valid input")
