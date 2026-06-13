Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,4,5,6,7,8,9,99,999,9999}
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 999, 9999}
s.add(100)
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 999, 100, 9999}
sort(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sort(s)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
s.sort()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.sort()
AttributeError: 'set' object has no attribute 'sort'
s.sorted()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.sorted()
AttributeError: 'set' object has no attribute 'sorted'
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 999, 100, 9999}
s.pop(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.pop(1)
TypeError: set.pop() takes no arguments (1 given)
s.add('string')
s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 999, 100, 'string', 9999}
999 in s
True
"string" is not s
True
'string' is not s
True
'string' in s
True
'string'  not in  s
False
for i in range(s)
SyntaxError: expected ':'
for i in range('s')
SyntaxError: expected ':'
for in s:
    
SyntaxError: invalid syntax
for i in s
SyntaxError: expected ':'
for i in s:
    print i
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(i)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
for i in s
SyntaxError: expected ':'
for i in s:
    print(i)

    
1
2
3
4
5
6
7
8
9
99
999
100
string
9999
d={1, 2, 3, 4, 5, 6, 7, 9999}
d
{1, 2, 3, 4, 5, 6, 7, 9999}
#subet means lesthan
{1}
{1}
{1}<s
True
{5}>d
False
s.injection (d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.injection (d)
AttributeError: 'set' object has no attribute 'injection'. Did you mean: 'intersection'?
s.intersection(d)
{1, 2, 3, 4, 5, 6, 7, 9999}
s.union(d)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 'string', 9999, 99, 100, 999}
s-d
{99, 100, 'string', 999, 8, 9}
s+d
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s+d
TypeError: unsupported operand type(s) for +: 'set' and 'set'
s.isdisajoint(d)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.isdisajoint(d)
AttributeError: 'set' object has no attribute 'isdisajoint'. Did you mean: 'isdisjoint'?
s.isdisjoint(d)
False
s.pop()
1
s.pop()
2
s
{3, 4, 5, 6, 7, 8, 9, 99, 999, 100, 'string', 9999}
ss.pop(9999)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    ss.pop(9999)
NameError: name 'ss' is not defined. Did you mean: 's'?
s
{3, 4, 5, 6, 7, 8, 9, 99, 999, 100, 'string', 9999}
s.pop(9999)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.pop(9999)
TypeError: set.pop() takes no arguments (1 given)
>>> s.remove(999)
>>> s
{3, 4, 5, 6, 7, 8, 9, 99, 100, 'string', 9999}
>>> max(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    max(s)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> s.clear()
>>> s
set()
>>> s.clear()
>>> 
>>> 
>>> s
set()
>>> a={1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 999, 100,9999}
>>> 
...     
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 999, 9999}
>>> b={1, 2, 3, 4, 5,9999}
>>> b
{1, 2, 3, 4, 5, 9999}
>>> a.intersection(b)
{1, 2, 3, 4, 5, 9999}
>>> a.intersection_update(b)
>>> a
{1, 2, 3, 4, 5, 9999}
>>> c=b
>>> c
{1, 2, 3, 4, 5, 9999}
>>> max(c)
9999
>>> min(c)
1
>>> c.add(14)
>>> c
{1, 2, 3, 4, 5, 14, 9999}
>>> len(c)
7
>>> sorted(c)
[1, 2, 3, 4, 5, 14, 9999]
>>> sum(c)
10028
>>> frozen = ([1,2,3]
