Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name = input('Sameer')
Sameer
>>> name = input()
Sameer
>>> 
>>> Sameer
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Sameer
NameError: name 'Sameer' is not defined
>>> name = input()
Sameer
>>> name
'Sameer'
>>> name=input('sameer')
sameer
>>> type(name)
<class 'str'>
>>> age = input()
23
>>> age
'23'
>>> '23'
'23'
>>> 
>>> age = input('enter the age: ')
enter the age: 23
>>> age
'23'
>>> type()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(age)
<class 'str'>
>>> cost = float(input ('enter the cost : '))
enter the cost : 1999.12
>>> cost
1999.12
>>> type(cost)
<class 'float'>
>>> #now we are using .split (to get soace for the values)
>>> 
>>> cost = float(input ('enter the cost : .split'))
enter the cost : .split
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    cost = float(input ('enter the cost : .split'))
ValueError: could not convert string to float: ''
cost = float(input ('enter the cost : ').split)
enter the cost : 199.2 200.2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    cost = float(input ('enter the cost : ').split)
TypeError: float() argument must be a string or a real number, not 'builtin_function_or_method'
'abc dcf kjh oiu' .spilt
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    'abc dcf kjh oiu' .spilt
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
'abc dcf kjh oiu' .spilt('')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    'abc dcf kjh oiu' .spilt('')
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
'abc dcf kjh oiu'.spilt('')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    'abc dcf kjh oiu'.spilt('')
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
'abc dcf kjh oiu' .split('')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'abc dcf kjh oiu' .split('')
ValueError: empty separator
'abc dcf kjh oiu'.split(' ')
['abc', 'dcf', 'kjh', 'oiu']
enter the names: one two three
SyntaxError: invalid syntax
names = input()
names = input()
enter the names :
    
SyntaxError: invalid syntax
enter the names
SyntaxError: invalid syntax
names = input("enter the names: ")
enter the names: one two three
names
'one two three'
numbers = input("enter the numbers: ")
enter the numbers: 
numbers = input("enter the numbers: ") .split('')
enter the numbers: 1254
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    numbers = input("enter the numbers: ") .split('')
ValueError: empty separator
numbers = input("enter the numbers: ").split('')
enter the numbers: 125
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    numbers = input("enter the numbers: ").split('')
ValueError: empty separator
numbers = input(("enter the numbers: ") .split(''))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    numbers = input(("enter the numbers: ") .split(''))
ValueError: empty separator
numbers = tuple(map(int,input("enter the numbers: ").split('')))
enter the numbers: 14 52
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    numbers = tuple(map(int,input("enter the numbers: ").split('')))
ValueError: empty separator
numbers = tuple(map(int,input("enter the numbers:").split('')))
enter the numbers:14 54
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    numbers = tuple(map(int,input("enter the numbers:").split('')))
ValueError: empty separator
ValueError: empty separator
SyntaxError: invalid syntax
numbers = tuple(map(int,input("enter the numbers:").split('')))
enter the numbers:
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    numbers = tuple(map(int,input("enter the numbers:").split('')))
ValueError: empty separator
numbers = tuple(map(int,input("enter the numbers:").split()))
enter the numbers:14 51
numbers
(14, 51)
numbers = tuple(map(float,input("enter the numbers:").split()))
enter the numbers:1.2 2.1
numbers
(1.2, 2.1)
numbers = set(map(int,input("enter the numbers:").split()))
enter the numbers:1 25 
numbers
{1, 25}
numbers = set(map(float,input("enter the numbers:").split()))
enter the numbers:1.2 5231.21
numbers
{1.2, 5231.21}
a,b,c=list(map(int,input().split()))
a,b,c=list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a,b,c=list(map(int,input().split()))'
a,b,c=list(map(int,input("enter the numbers:").split()))
enter the numbers:1 2 3
a
1
c
3
b
2
email,password=['same@gmail.com,pass$12']
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    email,password=['same@gmail.com,pass$12']
ValueError: not enough values to unpack (expected 2, got 1)

b=eval(input())
ABC
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'ABC' is not defined
b=eval(input("enter the name:"))
enter the name:AABC
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b=eval(input("enter the name:"))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'AABC' is not defined
b=eval(input("enter the input:"))
enter the input:[1 2 32]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    b=eval(input("enter the input:"))
  File "<string>", line 1
    [1 2 32]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
SyntaxError: invalid syntax. Perhaps you forgot a comma?
SyntaxError: invalid syntax
b=eval(input("enter the input: "))
enter the input: [1 2 58]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b=eval(input("enter the input: "))
  File "<string>", line 1
    [1 2 58]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b=eval(input("enter the input:"))
enter the input:[1,2,35987]
b
[1, 2, 35987]
b=eval(input("enter the input:"))
enter the input:[1.22 3.25 .6]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b=eval(input("enter the input:"))
  File "<string>", line 1
    [1.22 3.25 .6]
     ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b=eval(input("enter the input:"))
enter the input:[1.2,2.35,215.4,.235]
b
[1.2, 2.35, 215.4, 0.235]
b=eval(input("enter the input:"))
enter the input:[false]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b=eval(input("enter the input:"))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'false' is not defined. Did you mean: 'False'?
b=eval(input("enter the input:"))
enter the input:[true]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    b=eval(input("enter the input:"))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
b=eval(input("enter the input:"))
enter the input:true
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b=eval(input("enter the input:"))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
b=eval(input("enter the input:"))
enter the input: True
b
True
b=eval(input("enter the input:"))
enter the input:false
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    b=eval(input("enter the input:"))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'false' is not defined. Did you mean: 'False'?
b=eval(input("enter the input:"))
enter the input:False
b
False
a,b,c=10,10.3,'python'
a
10
b
10.3
c
'python'
print(a,b,c)
10 10.3 python
print("a =",a,"b =",b,"c =",c)
a = 10 b = 10.3 c = python
print("a =",a,"b =",b,"c =",c,sep='\n')
a =
10
b =
10.3
c =
python
print("a =",a,"b =",b,"c =",c,sep)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print("a =",a,"b =",b,"c =",c,sep)
NameError: name 'sep' is not defined. Did you mean: 'set'?
print("a =",a,"b =",b,"c =",c,sep='')
a =10b =10.3c =python
print("a =",a,"b =",b,"c =",c,sep='@')
a =@10@b =@10.3@c =@python
print("a =",a,"b =",b,"c =",c,sep='@\n')
a =@
10@
b =@
10.3@
c =@
python
print("a =",a,"b =",b,"c =",c,sep='@',end='...........................')
a =@10@b =@10.3@c =@python...........................
print(f'a={a} b={b} c={c})
      
SyntaxError: unterminated f-string literal (detected at line 1)
