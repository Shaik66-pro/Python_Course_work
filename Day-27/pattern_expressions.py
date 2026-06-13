'''
import re

name = input("enter the name : ")
pattern = r'^[A-Za-z]{2,25} ([A-Za-z]{2,25})+$'
print("Valid Name" if re.fullmatch(pattern, name) else "Invalid Name")
'''
'''
import re

email = input("Enter the E-mail: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("Valid Email" if re.fullmatch(pattern, email) else "Invalid Email")
'''
'''
import re
password = input("Enter the password: ")
#pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&] {8,}$'
print("Valid Password" if re.fullmatch(pattern, password) else "Invalid Password")
'''
'''
import re

phone = input("Enter Phone Number: ")

pattern = r'^\+91[6-9]\d{9}$'

print("Valid Number" if re.fullmatch(pattern, phone) else "Invalid Number")
'''
'''
import re

username = input("Enter Username: ")

pattern = r'^[A-Za-z][A-Za-z0-9_]{4,14}$'

print("Valid Username" if re.fullmatch(pattern, username) else "Invalid Username")
'''
