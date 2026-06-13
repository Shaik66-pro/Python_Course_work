class Instagram:
    def __init__(self,username,password,email):
        self.username = username
        self._email = email
        self.__password = password
        print(f'HI {self.username}, Welcome To Instagram. Follow Your 5 Friends')


    @property
    def emailaccess(self):
        return self._email
    
    @emailaccess.setter
    def emailaccess(self,new_email):
        self._email = new_email
        
    def getpassword(self):
        return self.__password
    
    def setpassword(self,new_password):
        self.__password = new_password


priya = Instagram('priya', 'priya@123', 'priya123@gmail.com')
print('Before username:' ,priya.username)
priya.username = 'bhavana'
print('After username :' ,priya.username)

print('Before Email   :' ,priya.emailaccess)
priya.email = 'bhavana@gmail.com'
print('After Email    :' ,priya.emailaccess)

print('Before Password:', priya.getpassword())
priya.setpassword('bhavana@123')
print('After Password :', priya.getpassword()) 

