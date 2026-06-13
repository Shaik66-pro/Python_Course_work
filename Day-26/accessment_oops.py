'''
from abc import ABC,abstractmethod
class Person:
    def __init__(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    @abstractmethod
    def displayInfo(self):
        pass

class Teacher(Person):
    def __init__(self,name,phonenumber,subject,salary):
        super().__init__(name,phonenumber)
        self.subject = subject
        self.salary = salary
    def displayInfo(self):
        print("----------Teacher Information------------")
        print(f" Name         : {self.name}")
        print(f" Phone Number : {self.phonenumber}")
        print(f" Subject      : {self.subject}")
        print(f" Salary       : {self.salary}")
        
class Student(Person):
    def __init__(self,name,phonenumber,grades,rollnumber):
        super().__init__(name,phonenumber)
        self.grades = grades
        self.rollnumber = rollnumber
    @staticmethod
    def check(g):
        if g == 'A':
            return "A Grade - Very Bad, We Don't You"
        elif g == 'B':
            return "B Grade - Bad, We Don't You Too"
        elif g == 'C':
            return "C Grade - Good, Keep Going"
        elif g == 'D':
            return "D Grade - Very , Keep Going !! No One Can Stop You"
        elif g == 'F':
            return "F Grade - Very , Excellent !! Your Way, One Way "
    def displayInfo(self):
        print("----------Student Information------------")
        print(f" Name         : {self.name}")
        print(f" Phone Number : {self.phonenumber}")
        print(f" Grades       : {self.grades}")
        print(f" Roll Number  : {self.rollnumber}")


sameer = Teacher('Sameer', '9876543210', 'Ethics', 56789)
sameer.displayInfo()

Nawab = Student('Nawab', '9876543210', 'F', 69)
Nawab.displayInfo()
'''
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,phonenumber,gender,email):
        self.name = name
        self.phonenumber = phonenumber
        self.gender = gender
        self.email = email

    @abstractmethod
    def displayInfo(self):
        pass
class Passenger(Person):
    def __init__(self,name,phonenumber,gender,email,source,destination,seatno):
        super().__init__(name,phonenumber,gender,email)
        self.source = source
        self.destination = destination
        self.seatno = seatno
    def displayInfo(self):
        print("--------Passenger Details---------")
        print(f"Name        : {self.name}")
        print(f"PhoneNumber : {self.phonenumber}")
        print(f"Gender      : {self.gender}")
        print(f"Email       : {self.email}")
        print(f"Source      : {self.source}")
        print(f"Destination : {self.destination}")
        print(f"SeatNo      : {self.seatno}")
class Driver(Person):
    def __init__(self,name,phonenumber,gender,email):
        super().__init__(name,phonenumber,gender,email)
    def displayInfo(self):
        print("--------Bus Driver Details---------")
        print(f"Name        : {self.name}")
        print(f"PhoneNumber : {self.phonenumber}")
        print(f"Gender      : {self.gender}")
        print(f"Email       : {self.email}")
class BusDetails:
    def __init__(self,name,busnumber,bustype,ticketprice,availableseats):
        self.name = name
        self.busnumber = busnumber
        self.bustype = bustype
        self.ticketprice = ticketprice
        self.availableseats = availableseats
    def displayInfo(self):
        print("--------Bus Details---------")
        print(f"Name          : {self.name}")
        print(f"BusType       : {self.bustype}")
        print(f"BusNumber     : {self.busnumber}")
        print(f"TicketPrice   : {self.ticketprice}")
        print(f"AvailableSeats: {self.availableseats}")
class Payment:
    def __init__(self,UPI_ID,UPI_PIN,Amount,Message):
        self.UPI_ID = UPI_ID
        self.UPI_PIN = UPI_PIN
        self.Amount = Amount
        self.message = Message
    def displayInfo(self):
        print("--------Payment Details---------")
        print(f" UPI_ID       : {self.UPI_ID}")
        print(f"Amount        : {self.Amount}")
        print(" Payment Succesfull ")
        print(f"Message       : {self.message}")

passenger = Passenger("Sameer Nawab","9876543210","Male","Sameernawab66@gmail.com","Hyderabad","Dubai ---Habbibi--",69)
passenger.displayInfo()
       
driver = Driver("Miya Bhai","98765768210","Male","Sameernawab66@gmail.com")
driver.displayInfo()

bus = BusDetails("Habbibi Travels","TG 08 E 0845","Sleeper",2500,6)
bus.displayInfo()

payment = Payment("567rty678gh67","999",2500,"After Ticket Confirms !! No Cancellation !! No Refunds !! ")
payment.displayInfo()
