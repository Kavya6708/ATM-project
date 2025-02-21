from ATM import DepositError,WithDrawError,InSufFoundError
from ATMMenu import menu
from ATMoperation import deposit, withdraw,balenq

while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Don't Try To Deposit alnums,strs and symbols")
                except DepositError:
                    print("Don't Enter -ve and Zero as Deposit Amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("don't try to Withdraw alnums,strs and symbols")
                except WithDrawError:
                    print("Don't Enter -ve and zero as withdraw Amount")
                except InSufFoundError:
                    print("Ur Account XXXXXXX123 Does Not Have that Much Money")
            case 3:
                    balenq()
            case 4:
                print("Tnx for this application")
                break
            case _ :
                print("Ur selection of operation is wrong---try again")
    except ValueError:
        print("Ur Account XXXXXXX123 Does Not Have that Much Money")

