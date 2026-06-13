'''n = 0
try:
    n +=10
except NameError:
    print("varaible is not defined ")
else:
    print("No Error ")
finally:
    print("End of the Programming ")
'''
'''
try:
    n +=10
    a = int(input("Enter the number: "))
    #l = [1,2,3,4,5]
    print(1[10])
    #k = {1:1,2:2,3:3,4:4}
    m = 10+'a'
except (NameError,TypeError,) as e :
    print(f'Error Occured : {e}')
else:
    print("No Error ")
finally:
    print("End of the Programming ")
    
'''

'''
try:
    n +=10
    a = int(input("Enter the number: "))
    #l = [1,2,3,4,5]
    print(1[10])
    #k = {1:1,2:2,3:3,4:4}
    m = 10+'a'
except Exception as e :
    print(f'Error Occured : {e}')
else:
    print("No Error ")
finally:
    print("End of the Programming ")
    
'''

'''
try:
   balance = 100
   wd = -2000
   if wd < 0:
       raise Exception("Please Enter Positive Number : ")
except Exception as e :
    print(f'Error Occured : {e}')
else:
    print("No Error ")
finally:
    print("End of the Programming ")
'''

# file operations : open,close,write,read and append

with open('pfs-52.txt', 'r') as file:
    print(file.readline())

    file.seek(0)
    print(file.readlines())

    file.seek(0)
    print(file.read())






































