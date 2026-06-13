# calcluator.py
def addditon(a,b):
    return a+b
def subtraction(a,b):
    return a-b
# main.py
import calculator as c
a,b = list(map(int,input()).split())
print("Addition :", addtion(a,b))
print("Subtraction :", subtraction(a,b))


import math
import random

n = int(input())
print("Square is : ", math.sqrt(n))
print("Random Number : ", random.randint(1,10))


try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")





with open("student.txt", "w+") as file:
    name = input()
    file.write(name)
    file.seek(0)
    print(file.read(),"written and displayed from file")




s = input()
vow  = "aeiouAEIOU"
c = 0
for i in s:
    if i in vol:
        c += 1
print(c)
