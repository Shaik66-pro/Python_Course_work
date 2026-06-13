'''
def add(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)
    
def mul(a,b):
    print(a*b)
    
def div(a,b):
    print(a/b)
'''

data = {
    12345:{'pin':1245,'balance':5000,'histroy':[]},
    23456:{'pin':1245,'balance':15000,'histroy':[]},
    34567:{'pin':1245,'balance':25000,'histroy':[]},
    64589:{'pin':1245,'balance':35000,'histroy':[]}
    }
acc_num = None

def login(e_num,e_pin):
    if e_num in data and data[e_num]['pin']==e_pin:
        print("Login Successfull")
        global acc_num
        acc_num = e_num
        return True
    else:
        print("invalid Login")
        return False

def check_balance():
    print("Current Balance",data[acc_num]['balance'])
def deposit():
    amount = int(input("Enter the deposit amount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} is deposited +++++++++')
    print("Deposit Successfull")
def withdraw():
    amount = int(input("Enter the withdraw amount: "))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['history'].append(f'{amount} is withdraw +++++++++')
        print("Withdraw Successfull")
    else:
        print("Insufficent BAlance")
def viewtransaction():
    if data[acc_num]['history']:
        print("----------------Transcation Hsitory-------------------")
        for i in data[acc_num]['history']:
            print(i)
        print("----------------End of the history---------------------")
    else:
        print("No Transaction")
