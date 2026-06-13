Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='sameer'
for i in s:
    print(i)

    
s
a
m
e
e
r
\
s1="sameer"
for j in s1:
    print(s1)

    
sameer
sameer
sameer
sameer
sameer
sameer
s2='sameer'
for t in s2:
    print(s2)

    
sameer
sameer
sameer
sameer
sameer
sameer
k={1:1,2:4,3:3,4:5,5:8}
for i in k:
    print(i,k[i])

    
1 1
2 4
3 3
4 5
5 8
for i in range(1,10,3):
    print(i)

    
1
4
7
for i in range(1,100,3):
print(i)
SyntaxError: expected an indented block after 'for' statement on line 1
for i in range(1,100,3):
    print(i)

    
1
4
7
10
13
16
19
22
25
28
31
34
37
40
43
46
49
52
55
58
61
64
67
70
73
76
79
82
85
88
91
94
97
for i in range(100,1,3):
    print(i)

    




for i in range(100,1,-3):
    print(i)

    
100
97
94
91
88
85
82
79
76
73
70
67
64
61
58
55
52
49
46
43
40
37
34
31
28
25
22
19
16
13
10
7
4
for i in range(1,100):
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
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
for i in range(2*2,200):
    print(i)

    
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
a=('python')
for i in a enumerate(a):
    
SyntaxError: invalid syntax
for i in  enumerate(a):
    print(i)

    
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
for i in  range(len(a):
    print(i)
                
SyntaxError: invalid syntax
for i in range(len(a):
    print(i)
               
SyntaxError: invalid syntax
for i in range(len(a):
    print(i,s[a])
               
SyntaxError: invalid syntax
for i in range(len(a)):
    print(i,s[a])

               
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    print(i,s[a])
TypeError: string indices must be integers, not 'str'
for i in range(len(a)):
    print(i[0],s[a])

               
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    print(i[0],s[a])
TypeError: 'int' object is not subscriptable
for i in range(len(a)):
    print(i,s[a])

               
Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    print(i,s[a])
TypeError: string indices must be integers, not 'str'
a
               
'python'
names = ['sameer','sai','teja']
               
for i in range(len(names)):
               print(i)

               
0
1
2
for i in range(len(names)):
               print(i,names[i])

               
0 sameer
1 sai
2 teja
q={1,2,3,4}
               
for i in enumerate(q):
               print(i[0],i[1])

               
0 1
1 2
2 3
3 4
z={1:2,2:3,3:4,4:5}
               
for i in enumerate(z):
               print(i)

               
(0, 1)
(1, 2)
(2, 3)
(3, 4)
for i in enumerate(z):
               print(i[0],i[1],z[i[1]])

               
0 1 2
1 2 3
2 3 4
3 4 5
for i in range(10):
               pass

               

for i in range(10):
               if i==15:
               skip
               
SyntaxError: expected an indented block after 'if' statement on line 2

for i in range(10):
               if i==5:
               break
            
SyntaxError: expected an indented block after 'if' statement on line 3
for i in range(10):
               if i==5:
               break
            print(i)
            
SyntaxError: expected an indented block after 'if' statement on line 2
for i in range(10):
     if i==5:
        break
    print(i)
    
SyntaxError: unindent does not match any outer indentation level
for i in range(10):
    if i==5:
        break
    print(i)

    
0
1
2
3
4
for i in range(10):
    if i==5:
        continue
    print(i)

    
0
1
2
3
4
6
7
8
9
for i in range(10):
    if i==9:
        break
    print(i)

    
0
1
2
3
4
5
6
7
8
pin=12345
for i in range:
    epin=int(input("enter the pin:")
             if pin==epin:
             
SyntaxError: '(' was never closed
pin=12345
for i in range:
    epin=int(input("enter the pin:")
             if pin==epin:
             
SyntaxError: multiple statements found while compiling a single statement
pin=12345
for i in range:
    epin=int(input("enter the pin:")
             if pin==epin:
             
SyntaxError: multiple statements found while compiling a single statement
pin=12345
for i in range:
    epin=int(input("enter the pin:")
...              if pin==epin :
...              
SyntaxError: multiple statements found while compiling a single statement
>>> pin=12345
... for i in range:
...     epin=int(input("enter the pin:")
...              if pin==epin:
...              
SyntaxError: multiple statements found while compiling a single statement
>>> pin=12345
... for i in range:
...     epin=int(input("enter the pin:")
...      if pin==epin:
...              
SyntaxError: multiple statements found while compiling a single statement
>>> pin=12345
... for i in range:
...     epin=int(input("enter the pin:")
...  if pin==epin:
...              
SyntaxError: multiple statements found while compiling a single statement
>>> del pin
...              
>>> pin=12345
... for i in range:
...     epin=int(input("enter the pin:")if pin==epin:
...              
SyntaxError: multiple statements found while compiling a single statement
>>> pin=12345
... for i in range:
...     epin=int(input("enter the pin:")
...     if pin==epin:
...              
SyntaxError: multiple statements found while compiling a single statement
>>> pin = 12345
... 
... for i in range(3):
...     epin = int(input("Enter the pin: "))
...     
...     if pin == epin:
...         print("Access granted")
...         break
...     else:
...         print("Wrong pin")
...         
SyntaxError: multiple statements found while compiling a single statement
