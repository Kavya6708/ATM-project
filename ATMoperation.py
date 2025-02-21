#ATMoperation.py
from ATM import DepositError,WithDrawError,InSufFoundError
bal=500-0
def deposit():
    damt=float(input("Enter Ur Deposit Amount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account XXXXXXX123 Deposit with INR:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter Ur withdraw Amount:"))
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSufFoundError
    else:
        bal=bal-wamt
        print("Ur Account XXXXXXX123 Debited With INR:{}".format(bal))
        print("Now Ur Account XXXXXXX123 Balance is INR:{}".format(bal))
def balenq():
    print("Ur Account XXXXXXX123 Balance INR:{}".format(bal))


