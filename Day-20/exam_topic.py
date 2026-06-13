'''
1.from functions
2.recursions
3. we have 2 questions in lambda
4. list comphresion we have 2 questions
5. generators
'''
'''
def fib(n):
    if n<1:
        return
    elif n==1:
        print(0)
    elif n>=2:
        a,b=0,1
        print(a,b,end =' ')
        for i in range(n-2):
            c=a+b
            print(c,end =' ')
            a,b=b,c

n = int(input("Enter the number: "))
fib(n)
'''
'''
def sumofn(n):
    s=0
    for i in range(1,n+1):
        s+=i
    print(f"sum of {n} numbers : {s}")

n = int(input("Enter the number: "))
sumofn(n)
'''

'''
def countvowels(n):
    c = 0
    vol = 'aeiouAEIOU'
    for i in n:
        if i in vol:
            c += 1
    print(f"number of vowels in {n} : {c}")
n = input("Enter the string : ")
countvowels(n)
'''
def sod(s):
    if s ==0:
        return 0
    return s%10+sod(s//10)
s = 12345
print(sod(s))
