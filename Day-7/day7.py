Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1.2,2.3,[1,2,3,4],{1,2,3})
t
(1.2, 2.3, [1, 2, 3, 4], {1, 2, 3})
len(t)
4
max(t)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'list' and 'float'
min(t)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'list' and 'float'
sort(t)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sort(t)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sortted(t)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sortted(t)
NameError: name 'sortted' is not defined. Did you mean: 'sorted'?
t=(1, 2, [1, 2, 3, 4], {1, 2, 3})
t
(1, 2, [1, 2, 3, 4], {1, 2, 3})
min(t)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'list' and 'int'
t=(1, 2, 1, 2, 3, 4, 1, 2, 3)
t
(1, 2, 1, 2, 3, 4, 1, 2, 3)
min(t)
1
max(t)
4
count(t)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(t)
NameError: name 'count' is not defined. Did you mean: 'round'?
t.count()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
c.count(4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c.count(4)
NameError: name 'c' is not defined
t.count(5)
0
t.count(4)
1
t1=(1,2,3,[4,5])
t1
(1, 2, 3, [4, 5])
t1.append(3,41)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t1.append(3,41)
AttributeError: 'tuple' object has no attribute 'append'
t1.append(41)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t1.append(41)
AttributeError: 'tuple' object has no attribute 'append'
t1.append('41')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t1.append('41')
AttributeError: 'tuple' object has no attribute 'append'
t1[4].append(41)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t1[4].append(41)
IndexError: tuple index out of range
t1[3].append(41)
t1
(1, 2, 3, [4, 5, 41])
t1.pop(41)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t1.pop(41)
AttributeError: 'tuple' object has no attribute 'pop'
t1[3].pop()
41
t1
(1, 2, 3, [4, 5])
t2={}
type(t2)
<class 'dict'>
s[1]='int'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s[1]='int'
NameError: name 's' is not defined
s={}
s
{}
d={}
d
{}
type(d)
<class 'dict'>
d={'name':'asif','batch':52,'skills':['python','css','html']}
d
{'name': 'asif', 'batch': 52, 'skills': ['python', 'css', 'html']}
d['name']='mehaboob'
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html']}
s={}
s
{}
s[1]='int'
s
{1: 'int'}
s[1.2]='float'
s
{1: 'int', 1.2: 'float'}
s[1+2m]='complex'
SyntaxError: invalid decimal literal
s[1+m]='complex'
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s[1+m]='complex'
NameError: name 'm' is not defined
s
{1: 'int', 1.2: 'float'}
s[{1:2,2:64}]='dict'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s[{1:2,2:64}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
s[(1,2,3)]='tuple'
s
{1: 'int', 1.2: 'float', (1, 2, 3): 'tuple'}
s[{12,54}]='set'
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s[{12,54}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
s
{1: 'int', 1.2: 'float', (1, 2, 3): 'tuple'}
'tuple'in s
False
'int'in s
False
s['int']
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s['int']
KeyError: 'int'
e={'name'='sameer','batch'=52,'skills'=['html css sql'],course='python'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

e={'name'='sameer','batch':52,'skills'=['html css sql'],course='python'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
e={'name'='sameer','batch':52,'skills':['html css sql'],course:'python'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
e={'name':'sameer','batch':52,'skills':['html css sql'],course:'python'}
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    e={'name':'sameer','batch':52,'skills':['html css sql'],course:'python'}
NameError: name 'course' is not defined
e={'name'='sameer','batch':52,'skills':['html css sql'],'course':'python'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
e={'name':'sameer','batch':52,'skills':['html css sql'],'course':'python'}
e
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql'], 'course': 'python'}
e.get('age')
e.get('course')
'python'
e,get('name')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    e,get('name')
NameError: name 'get' is not defined. Did you mean: 'set'?
e.get('name')
'sameer'
e.get('name,age','no age is present')
'no age is present'
e['course']='java'
e
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql'], 'course': 'java'}
e.popitem('course')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    e.popitem('course')
TypeError: dict.popitem() takes no arguments (1 given)
e.pop('course')
'java'
e
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
e.clear()
e
{}
e.update({'k2:k1','l1:l2'})
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    e.update({'k2:k1','l1:l2'})
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> e={}
>>> type()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(e)
<class 'dict'>
>>> e.update({'k2:k1','l1:l2'})
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    e.update({'k2:k1','l1:l2'})
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> e.keys()
dict_keys([])
>>> e.keys({'name': 'sameer', 'batch': 52, 'skills': ['html css sql']})
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    e.keys({'name': 'sameer', 'batch': 52, 'skills': ['html css sql']})
TypeError: dict.keys() takes no arguments (1 given)
>>> e={'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
>>> e
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
>>> e.keys()
dict_keys(['name', 'batch', 'skills'])
>>> {'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
>>> {'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}.keys()
dict_keys(['name', 'batch', 'skills'])
>>> len('e')
1
>>> sorted(e)
['batch', 'name', 'skills']
>>> len(e)
3
>>> e.get('name')
'sameer'
>>> e.setdefault('name','')
'sameer'
>>> e
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
>>> e
{'name': 'sameer', 'batch': 52, 'skills': ['html css sql']}
