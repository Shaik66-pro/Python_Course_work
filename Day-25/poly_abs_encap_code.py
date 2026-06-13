'''  #method overloading -------------------poly morphism
class Hotstar:
    def login(self):
        print("u can login")
    def sereach(self):
        print("u can sereach for the movies")
    def otp(self):
        print("u can verify the otp")
    def movies(self):
        print("limited movies u can watch")
    def users(self):
        print("limited users")
    def videocontrollers(self):
        print("ads will appears while watching video")
class PremiumHotstar(Hotstar):
    def movies(self):
        print("un-limited movies u can watch")
    def users(self):
        print("un-limited users")
    def videocontrollers(self):
        print("no ads will appears while watching video")

bhavana = Hotstar()
bhavana.login()
bhavana.users()
bhavana.otp()
bhavana.movies()
bhavana.videocontrollers()


sameer = PremiumHotstar()
sameer.login()
sameer.users()
sameer.otp()
sameer.movies()
sameer.videocontrollers()
    

class Number():
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num
    def __sub__(self,other):
        return self.num - other.num
    def __mul__(self,other):
        return self.num * other.num
    def __gt__(self,other):
        return self.num > other.num
    def __lt__(self,other):
        return self.num < other.num
    def __eq__(self,other):
        return self.num == other.num
    def __str__(self):
        return f'{self.num}'

a = Number(15)
b = Number(5)
print(a+b)
print(a-b)
print(a*b)
print(a>b)
print(a<b)
print(a==b)
print(a,b)
'''
from abc import ABC,  abstractmethod
class Payment(ABC):
    def input(self):
        print("Enter the amount")
    @abstractmethod
    def checkbalance(self):
        pass
    @abstractmethod
    def pin(self):
        pass
    
class UPI(Payment):
    def checkbalance(self):
        print("check balance of upi")
    def pin(self):
        print("verify the upi pin")
    
class Cards(Payment):
    def checkbalance(self):
        print("check balance for card transcation")
    def pin(self):
        print("otp is verifed , you can transfer the fund")
        
class NetBanking(Payment):
    def checkbalance(self):
        print("check balance of netbanking")
    def pin(self):
        print("verify the pin for netbanking")
        
class Wallet(Payment):
    def checkbalance(self):
        print("check balance in wallet")
    def pin(self):
        print("verify the wallet pin")

bhavana = UPI()
bhavana.checkbalance()
bhavana.pin()

sameer = Cards()
sameer.checkbalance()
sameer.pin

yashwanth = Wallet()
yashwanth.checkbalance()
yashwanth.pin()

















































































