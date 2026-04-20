Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
S=''
S
''
fname=avb
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fname=avb
NameError: name 'avb' is not defined
fname='abg'
lname='kjn'
fnam+lname
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fnam+lname
NameError: name 'fnam' is not defined. Did you mean: 'fname'?
fname+lname
'abgkjn'
fnam-lname
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fnam-lname
NameError: name 'fnam' is not defined. Did you mean: 'fname'?
fnam*8+lname*7
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fnam*8+lname*7
NameError: name 'fnam' is not defined. Did you mean: 'fname'?
fnam*8
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fnam*8
NameError: name 'fnam' is not defined. Did you mean: 'fname'?
fname*8+lname*9
'abgabgabgabgabgabgabgabgkjnkjnkjnkjnkjnkjnkjnkjnkjn'
fname*8-lname*9
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fname*8-lname*9
TypeError: unsupported operand type(s) for -: 'str' and 'str'
fname*8/lname*9
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fname*8/lname*9
TypeError: unsupported operand type(s) for /: 'str' and 'str'
'Sameer'
'Sameer'
s='Sameer'
s[2]
'm'
TypeError: unsupported operand type(s) for /: 'str' and 'str'
SyntaxError: invalid syntax
s[4]
'e'
# this procces is called index it means to extract data from the string
s1= 'one two three'
s1[9]
'h'
s1[-9]
't'
s1[0]
'o'
# this procces is called index it means to extract data from the string to a particular value'
# slicin
names='one two three'
names[0:5]
'one t'
names[0:5:+1]
'one t'
names[:2]
'on'
names[:3]
'one'
names[4:6]
'tw'
names[4:7]
'two'
names[:-5]
'one two '
names[-3:]
'ree'
names[-4]
'h'
names[-4:]
'hree'
names[-5:]
'three'
names[:-5]
'one two '
names[-1:-5]
''
names[-5:-1]
'thre'
names[-2:-5:-1]
'erh'
#reverse of  a string
*/now/*
SyntaxError: invalid syntax
# now : member string oprerations
ord('')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
# member
o in name
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    o in name
NameError: name 'o' is not defined
'o' in name
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    'o' in name
NameError: name 'name' is not defined. Did you mean: 'fname'?
'o' in names
True
's' in names
False


    
        # to know the ascii values
        
odr(names)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    odr(names)
NameError: name 'odr' is not defined
ord('names')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ord('names')
TypeError: ord() expected a character, but string of length 5 found
len('names')
5
odr('names')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    odr('names')
NameError: name 'odr' is not defined

            # built in functions
            
#len()
            
len('names')
5
sorted('names')
['a', 'e', 'm', 'n', 's']
odr[4]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    odr[4]
NameError: name 'odr' is not defined
ord(n)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    ord(n)
NameError: name 'n' is not defined
name='leo das roman'
name
'leo das roman'
len(name)
13
name.upper()
'LEO DAS ROMAN'
name.lower()
'leo das roman'
name.capitalize()
'Leo das roman'
name.capitalize(4)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    name.capitalize(4)
TypeError: str.capitalize() takes no arguments (1 given)
name.title()
'Leo Das Roman'
name.swapcase()
'LEO DAS ROMAN'

            # alingment method
            
name.center(40,'^')
'^^^^^^^^^^^^^leo das roman^^^^^^^^^^^^^^'
name.center(40,' ')
'             leo das roman              '
name.ljust(40,'^')
'leo das roman^^^^^^^^^^^^^^^^^^^^^^^^^^^'
name.rjust(45,'+')
'++++++++++++++++++++++++++++++++leo das roman'
name.zfill(45)
'00000000000000000000000000000000leo das roman'
name
'leo das roman'
name.find('p')
-1
name('roman')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    name('roman')
TypeError: 'str' object is not callable
name.find('roman')
8
name.count('o")
           
SyntaxError: unterminated string literal (detected at line 1)
name.count('o')
           
2
name.count('m')
           
1
name.rfind('r')
           
8
name.lfind('g')
           
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    name.lfind('g')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
name.rfind('w')
           
-1
name.rfind('i')
           
-1
            # replace and modify method#
           
names
           
'one two three'
name.replace(a,'@')
           
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    name.replace(a,'@')
NameError: name 'a' is not defined
name.replace('a','@')
           
'leo d@s rom@n'
name.replace('leo','sameer')
           
'sameer das roman'
name.translate(aeious,'1234568')
           
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    name.translate(aeious,'1234568')
NameError: name 'aeious' is not defined
name.maketrans(aeious,'1238')
           
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    name.maketrans(aeious,'1238')
NameError: name 'aeious' is not defined
name.maketrans('aeious','1238')
           
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    name.maketrans('aeious','1238')
ValueError: the first two maketrans arguments must have equal length
name.translate('aeious','1238')
           
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    name.translate('aeious','1238')
TypeError: str.translate() takes exactly one argument (2 given)
name.maketrans('aeious','1238')
           
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    name.maketrans('aeious','1238')
ValueError: the first two maketrans arguments must have equal length
            #spliting and join#
           
name.split()
           
['leo', 'das', 'roman']
name.split(' ',3)
           
['leo', 'das', 'roman']
>>> name.rsplit(' ',4)
...            
['leo', 'das', 'roman']
>>> name.partition('m')
...            
('leo das ro', 'm', 'an')
>>> name.rpartition('o')
...            
('leo das r', 'o', 'man')
>>> name.lpartition('o')
...            
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    name.lpartition('o')
AttributeError: 'str' object has no attribute 'lpartition'. Did you mean: 'partition'?
>>> name.rpartition('e')
...            
('l', 'e', 'o das roman')
>>> s='     sameer           nawab')
SyntaxError: unmatched ')'
>>> s='     sameer           nawab'
>>> s
'     sameer           nawab'
>>> s.strip()
'sameer           nawab'
>>> s.rstrip()
'     sameer           nawab'
>>> s.lstrip()
'sameer           nawab'
>>>                                                  #encoding and decoding#
>>> 
>>> '🙉🙉'.encode()
b'\xf0\x9f\x99\x89\xf0\x9f\x99\x89'
>>> decode()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    decode()
NameError: name 'decode' is not defined
>>> b'\xf0\x9f\x99\x89\xf0\x9f\x99\x89' decode()
SyntaxError: invalid syntax
>>> b'\xf0\x9f\x99\x89\xf0\x9f\x99\x89' .decode()
'🙉🙉'
>>> '🐘🦣🦍🦧🦍'.encode()
b'\xf0\x9f\x90\x98\xf0\x9f\xa6\xa3\xf0\x9f\xa6\x8d\xf0\x9f\xa6\xa7\xf0\x9f\xa6\x8d'
>>> b'\xf0\x9f\x90\x98\xf0\x9f\xa6\xa3\xf0\x9f\xa6\x8d\xf0\x9f\xa6\xa7\xf0\x9f\xa6\x8d'.decode()
'🐘🦣🦍🦧🦍'
