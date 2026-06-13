'''
class A:
    def printa(self):
        print("Parent class - A")
class B:
    def printb(self):
        print("Child class - B")            #single inheritance


a = A()
a.printa()
b = B()
b.printb()
b.printa()




class A:
    def printa(self):
        print("Parent class - A")
class B(A):
    def printb(self):
        print("Class - B")           #multi-level inheritance
class C(B):
    def printc(self):
        print("Class - c")

c = C()
c.printa()
c.printb()
c.printc()


class A:
    def printa(self):
        print("Parent class - A")
class B(A):
    def printb(self):
        print("Class - B")           #multiple inheritance
class C(A):
    def printc(self):
        print("Class - c")
class D(A):
    def printd(self):
        print("Class - D")
a = A()
a.printa()
b = B()
b.printb()
c = C()
c.printc()
d = D()
d.printd()
'''

class A:
    def display(self):
        print("Class - A")
class C:
    def display(self):
        print("Class - C")
class B(A,C):
    def display(self):
        A.display(self)
        C.display(self)
        print("Class B")

b = B()
b.display()
