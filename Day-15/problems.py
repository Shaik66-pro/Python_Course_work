'''
a=15
b=12

prime=[]
for i in range(2,b+1):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        prime.append(i)
print(prime)

i=0
fact=1
while b not in prime:
    if b%prime[i]==0:
        b=b//prime[i]
    else:
        i=i+1
    fact*=prime[i]
    
print(fact*b)    
    
'''
'''
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
fact=[]
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        fact.append(i)
print(fact[-1])        
'''
'''
c = input("Enter the number: ")   
l = len(c)                        
arm = 0

for i in c:
    arm += int(i) ** l

print("Armstrong number" if int(c) == arm else "Not Armstrong number")    
'''
