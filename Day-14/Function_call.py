#int,float,string,list,tuple,set,dict,boolean

#mutable - changing refelecting the in and out - so  called as pass by reference
#immutable - changing not refelecting the in and out - so  called as pass by value
'''
def display():
    course = 'PFS'   
    
    print("Starting:", course)
    
    def change():
        nonlocal course
        course = 'JFS'
        print("Course Changed:", course)
    
    change()    
    print("Final:", course)

display()
'''
'''
s='python'
print(len(s))

print=23
print(len)
'''
'''
def display(i,s):
    if i==len(s):
        return 
    print(s[i:i:+5])     
    display(i+1,s)
    
    
s='python programming'
display(0,s)

'''

def display(n):
    if n==0:
        return 0
    return (n%10) + display(n//10)
    
print(display(123456789))
