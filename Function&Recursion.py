'''def calu_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calu_sum(2,3)

def print_hello():
    print('Hello')

print_hello()'''

#WAP to cal the avg of 3 nos.
'''def avg(a,b,c):
    average=(a+b+c)/3
    print(average)
    return average #kaam samajh nhi aaya

avg(1,2,3)'''

#product
'''def calcu_prod(a,b):
    prod=a*b
    print(prod)
    return prod

calcu_prod(6,8)'''

#practice questions
#WAF to print the length of a list. (list is the parameter)
'''yashi=[1,2,3,4,5,6,7,8,9,10]
def length(list):
    lengthoflist=len(list)
    print(lengthoflist)
    return lengthoflist

length(yashi)'''

#WAF to print the elements of a list in a single line
'''list1=[1,2,3,4,5,6]
def print_elements(list):
    for item in list1:
        print(item,end="")

print_elements(list1)'''

#WAF to find the factorial of n


'''def cal_factorial(n):
    fac=1
    for i in range(1,n+1):
        fac *= i
        print(fac)
    
    
cal_factorial(5)'''

#WAF to convert USD to INR
'''def conversion(r):
    inr=83*r
    print(inr)
    return inr

conversion(4)'''

#Homework Problem
'''def Type(n):
    if (n%2==0):
        print('EVEN')
    else:
        print('ODD')
'''

#RECURSION
#we have to print numbers from 5 to 1 using recursion

'''def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)'''

# returns n!
'''def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
'''

'''def sum(n):
    if (n==0):
        return 0
    else:
        return sum(n-1) + n

print(sum(10))
'''

def print_element(list,n=0):
    if (n==len(list)):
        return
    print(list[n])
    print_element(list,n+1)

yashi = [1,2,3,4,5,6]

print(print_element(yashi))