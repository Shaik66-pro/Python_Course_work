'''
import sys
print(sys.argv)
'''
#print(sys.argv)
#print(sys.path)
#print(sys.version)

'''
import sys
print('start')
sys.exit()
print('end')
'''
'''
import platform
print(platform.system())
print(platform.version())
print(platform.release())
print(platform.processor())
'''
'''
import math

print(math.pi)
print(math.e)
print(math.sqrt(4))
print(math.sqrt(64))
print(round(12.508784))
print(math.ceil(13.21548))
print(math.floor(13.2121))
print(math.floor(11.999))
print(abs(-30))
print(math.factorial(3))
'''
'''
import math
print(math.gcd(30,20,4))
print(math.log(2,2))
print(math.tan(45))
print(math.sin(30))

'''
'''
import random
random.seed(40)
print(random.random())
print(random.uniform(1,6))
print(random.randint(1,6))

l = ["sameer","is a","python"]
m = [1,2,3]
print(random.choices(l, m))
'''

import collections
'''
s ='python programming'
l = [1,2,3,4,5,6,7,8,9,11,12,13,14,45]
text = 'The OS module provides functions to int'
print(collections.Counter(text.split()))
print(collections.Counter(s))
'''
'''
a = 'python programming'
d=collections.defaultdict(int)
for i in a:
    d[i] += 1
    
print(d)
'''

'''
import collections
#queue
d = collections.deque([])
d.append(10)
d.append(20)
d.append(30)
d.append(45)
d.popleft()
d.popleft()
d.popleft()
d.append(19)
d.append(39)
print(d)

#stack
d = collections.deque([])
d.appendleft(10)
d.appendleft(20)
d.appendleft(30)
d.appendleft(45)
d.pop()
d.pop()
d.pop()
d.appendleft(19)
d.appendleft(39)
print(d)
'''
'''
e = collections.enqueue([])
e.append(10)
e.append(20)
e.append(30)
e.append(45)
e.popleft()
e.popleft()
e.popleft()
e.append(19)
e.append(39)
print(d)
'''

import itertools
print(list(itertools.combinations("ABCD",2)))
print(list(itertools.permutations("ABCD",2)))


