'''
password=input("enter the password:")
if len(password)>=8:
    status=set()
    for i in password:
        if i.islower():
                status.add('l')
        elif i.isupper():
                status.add('u')
        elif i.isdigit():
                status.add('d')
        else:
                status.add('s')
    if len(status)==4:
        print("Strong Password")
    else:
            print("weak password")
           '''
'''
products={
            1:{'Name':'rice','price':9},
            2:{'Name':'roti','price':19},
            3:{'Name':'chepati','price':29},
            4:{'Name':'yougert','price':39},
            5:{'Name':'chicken','price':49},
            6:{'Name':'bread','price':59},
            7:{'Name':'chocolate','price':69},
            8:{'Name':'dark ','price':79},
            9:{'Name':'mixed chocolate','price':89}
}
  
print("----------Welcome To Grocery store----------")'''                    
'''
i=1
while i<11:
    i=i+1
    if i==15:
        break
    print(i)
else:
        print('1...10 are printed')'''

'''
a=[1,0,2,2,0,0,0,0,0,0,0,0,0,0,5,7,9,6,98,4,6,9,10,100,0000,00000]
a.pop(a[0])
while 0 in a:
    a.remove(0)
print(a)
assert a<1==0,'value is assigned'
'''
q=12
assert q<10,'value is assigned'
