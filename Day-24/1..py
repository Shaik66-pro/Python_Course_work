Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 12, in <module>
    b.printb()
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 6, in printb
    printb("Child class - B")
NameError: name 'printb' is not defined. Did you mean: 'self.printb'?

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 13, in <module>
    b.printa()
AttributeError: 'B' object has no attribute 'printa'. Did you mean: 'printb'?

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 13, in <module>
    b.printa()
AttributeError: 'B' object has no attribute 'printa'. Did you mean: 'printb'?

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B
Parent class - A

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B
Class - c

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 30, in <module>
    a.printa()
NameError: name 'a' is not defined. Did you mean: 'A'?

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Child class - B
Class - c

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Class - B
Class - c

== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 44, in <module>
    class D(A,B,C):
TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B, C
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 49, in <module>
    d.printb()
AttributeError: 'D' object has no attribute 'printb'. Did you mean: 'printa'?
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 49, in <module>
    d.printb()
AttributeError: 'D' object has no attribute 'printb'. Did you mean: 'printa'?
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Parent class - A
Class - B
Class - c
Class - D
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Class - A
Class B
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Traceback (most recent call last):
  File "C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py", line 63, in <module>
    class B(A,C):
NameError: name 'C' is not defined. Did you mean: 'c'?
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Class - A
Class B
>>> 
== RESTART: C:/Users/samee/OneDrive/Desktop/Python_Course_Work/Day-23/inheritances_.py =
Class - A
Class - C
Class B
