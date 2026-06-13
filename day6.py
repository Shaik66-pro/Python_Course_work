Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'    ','shb'.isspace()
('    ', False)
('    ', False)
('    ', False)

.isspace()
SyntaxError: invalid syntax
s='python programming language'
s
'python programming language'
s.isaplha()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
s
'python programming language'
s.isstartwith(g)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.isstartwith(g)
AttributeError: 'str' object has no attribute 'isstartwith'. Did you mean: 'startswith'?
s.isstartswith(g)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.isstartswith(g)
AttributeError: 'str' object has no attribute 'isstartswith'. Did you mean: 'startswith'?
s.startswith(i)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.startswith(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
s.startswith('g')
False
s.endswith('l)
           
SyntaxError: unterminated string literal (detected at line 1)
s.endswith('l')
           
False
s.isalpha()
           
False
'sameer'.isalpha()
           
True
s.isnum()
           
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
s.isalnum()
           
False
'12345678'.isalnum()
           
True
'1234dfghj'.isalnum()
           
True
'sdfghjkl'.isalnum()
           
True
type('s')
           
<class 'str'>
s.islower()
           
True
'Sameer'.islower()
           
False
QWERTYUI.islower()
           
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    QWERTYUI.islower()
NameError: name 'QWERTYUI' is not defined
'QWERTYUIO'.islower()
           
False
'qweryui'.islower()
           
True
s.isupper()
           
False
s.title()
           
'Python Programming Language'
s.istitle()
           
False
s.isdentifier()
           
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.isdentifier()
AttributeError: 'str' object has no attribute 'isdentifier'. Did you mean: 'isidentifier'?
s.isidentifier()
           
False
                            */LIST*/
           
SyntaxError: unexpected indent
                            #list
           
l=[]
           
l=[1,2,3,4,5]
           
l
           
[1, 2, 3, 4, 5]
type(l)
           
<class 'list'>
a=[1.2.55,145,158,89]
           
SyntaxError: invalid syntax. Perhaps you forgot a comma?


a
           
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=[1,2,3,4]
           
b=[7,8,9]
           
print('a,b')
           
a,b
print(a,b)
           
[1, 2, 3, 4] [7, 8, 9]
a+b
           
[1, 2, 3, 4, 7, 8, 9]
(a+b)*8
           
[1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9, 1, 2, 3, 4, 7, 8, 9]
a+b*8
           
[1, 2, 3, 4, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9]
a*99+b*963
           

a*99 + b*963
           

a[::3]
           
[1, 4]
a[::::2]
           
SyntaxError: invalid syntax
a[::4]
           
[1]
a[:3]
           
[1, 2, 3]
'1' in a
           
False
'5' in a
           
False
len(a)
           
4
a={}
           
type('a')
           
<class 'str'>
type(a)
           
<class 'dict'>
type{a}
           
SyntaxError: invalid syntax
sorted(a)
           
[]
q=['sai qwerty das leo YSRCP']
           
Q
           
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    Q
NameError: name 'Q' is not defined. Did you mean: 'q'?
q
           
['sai qwerty das leo YSRCP']
sorted('q')
           
['q']
sorted(q)
           
['sai qwerty das leo YSRCP']
max(q)
           
'sai qwerty das leo YSRCP'
q=['sai' 'qwerty' 'das' 'leo' 'YSRCP']
           
q
           
['saiqwertydasleoYSRCP']
q=['sai','qwerty','das','leo','YSRCP']
           
q
           
['sai', 'qwerty', 'das', 'leo', 'YSRCP']
max(q)
           
'sai'
min(q)
           
'YSRCP'
id(q)
           
1473867188672
q.append('sameer')
           
q
           
['sai', 'qwerty', 'das', 'leo', 'YSRCP', 'sameer']
q.insert(4,'qalbi')
           
q
           
['sai', 'qwerty', 'das', 'leo', 'qalbi', 'YSRCP', 'sameer']
q.extend('ram','charan','sherkhan')
           
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    q.extend('ram','charan','sherkhan')
TypeError: list.extend() takes exactly one argument (3 given)
q.extend['ram','charan','sherkhan']
           
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    q.extend['ram','charan','sherkhan']
TypeError: 'builtin_function_or_method' object is not subscriptable
q.extend(['ram','charan','sherkhan'])
           
q
           
['sai', 'qwerty', 'das', 'leo', 'qalbi', 'YSRCP', 'sameer', 'ram', 'charan', 'sherkhan']
id(q)
           
1473867188672
q.append('yogi','ram','charan','sherkhan')
           
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    q.append('yogi','ram','charan','sherkhan')
TypeError: list.append() takes exactly one argument (4 given)
q.extend(1,'ram','charan','sherkhan')
           
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    q.extend(1,'ram','charan','sherkhan')
TypeError: list.extend() takes exactly one argument (4 given)
q.insert(1,'yogi','ram','charan','sherkhan')
           
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    q.insert(1,'yogi','ram','charan','sherkhan')
TypeError: insert expected 2 arguments, got 5
q
           
['sai', 'qwerty', 'das', 'leo', 'qalbi', 'YSRCP', 'sameer', 'ram', 'charan', 'sherkhan']
q.pop(5)
           
'YSRCP'
q
           
['sai', 'qwerty', 'das', 'leo', 'qalbi', 'sameer', 'ram', 'charan', 'sherkhan']
q.pop(0)
           
'sai'
q
           
['qwerty', 'das', 'leo', 'qalbi', 'sameer', 'ram', 'charan', 'sherkhan']
q.pop()
           
'sherkhan'
q
           
['qwerty', 'das', 'leo', 'qalbi', 'sameer', 'ram', 'charan']
q.remove('sameer')
           
q
           
['qwerty', 'das', 'leo', 'qalbi', 'ram', 'charan']
del q[3]
           
q
           
['qwerty', 'das', 'leo', 'ram', 'charan']
>>> q.clear()
...            
>>> q
...            
[]
>>> q
...            
[]
>>> q.restore()
...            
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    q.restore()
AttributeError: 'list' object has no attribute 'restore'
>>> q
...            
[]
>>> w
...            
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> w
...            
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> set()
...            
set()
>>> s
...            
'python programming language'
>>> q
...            
[]
>>> x=['sai', 'qwerty', 'das', 'leo', 'qalbi', 'YSRCP', 'sameer', 'ram', 'charan', 'sherkhan']
...            
>>> x
...            
['sai', 'qwerty', 'das', 'leo', 'qalbi', 'YSRCP', 'sameer', 'ram', 'charan', 'sherkhan']
>>> len(x)
...            
10
