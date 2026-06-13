'''
1.modules - built
2.user defined
3.exceptional handling
4.file exceptions
5.coding'''

#-------------------------------------------oops concept---------------------------------->
''''class flipkart:
    discount = 10
    products = ["men's bag","foot wear","travelling bags","pants","shoes","shorts"]
    @classmethod
    def showproducts(cls):
        for i in clsproducts(cls):
            print(i)
    @classmethod
    def showdiscount(cls):
        print("Discount:", cls.discount())
    def userinfo(self,username,phoneno):
        self.username = user
        self.phoneno = phoneno
        print(f"Welcome To The Flipkart {self.username}. shop now")
        
asif = flipkart()
priya = flipkart()
asif.userinfo("Asif",9876543210)

flipkart.showdiscount()
flipkart.showproducts()'''


class Flipkart:

    discount = 10

    products = [
        "men's bag",
        "foot wear",
        "travelling bags",
        "pants",
        "shoes",
        "shorts"
    ]

    @classmethod
    def showproducts(cls):
        for i in cls.products:
            print(i)

    @classmethod
    def showdiscount(cls):
        print("Discount:", cls.discount)

    def userinfo(self, username, phoneno):
        self.username = username
        self.phoneno = phoneno

        print(f"Welcome To The Flipkart {self.username}. Shop now")
    @staticmethod()
    def banner():
            print("10% discount is avaialable")


asif = Flipkart()
priya = Flipkart()

asif.userinfo("Asif", 9876543210)
asif.banner()
flipkart.banner

Flipkart.showdiscount()
Flipkart.showproducts()
