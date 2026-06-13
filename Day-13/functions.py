'''
def wish(name):
    print(f"Good After noon {name}" )
    print("Welcome To My world\t")
    
wish('Sameer')
wish('Priya')
wish('Asif')
'''
'''
def even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

even(11)
even(10)
'''

'''
def even(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'
    
print(even(12))
print(even(13))   
'''

'''
n=int(input("Enter the Number: "))
for i in range(2,n//2+1):
      if n%2==0:
          print('not prime number')
          break
      else:
          print('prime number')
      
'''
'''
def isprime(n):
    for i in range(2,n//2+1):
        if n%2==0:
            return False
        return True
    
print("prime number" if isprime(13) else "not prime")
print("prime number" if isprime(14) else "not prime")
'''
'''
def display(name,email,password,phoneno=None):
    print('Name:    ',name)
    print('Email:   ',email)
    print('Password:',password)
    print('phoneno: ',phoneno)
    
display('username','email@gmail.com','password','9876543210')
display('username','email@gmail.com','password')
'''
'''
def display(*n):
    print(sum(n))
display(1,2,3,6)
display(1,200,3,600)
display(1,2,30,60)'''
'''    
def display(**n):
    print(n)
display(k1='abc',k2='def')    
'''
