#printing hello 5 times
'''count = 1
while count <=5:
    print("Hello")
    count+=1

print(count)'''

#print numbers 1 to 5
'''c = 1

while c<=5:
    print(c)
    c+=1'''
#print numbers from 1 to 100
'''c=1
while c<=100:
    print(c)
    c+=1'''

#print numbers from 100 to 1
'''c=100
while c>=1:
    print(c)
    c-=1'''

#print the multiplication table of number n
'''i=1
n=int(input('Num:'))
while i<=10:
    print(n*i)
    i+=1'''

#printing the square of numbers from 1 to 10
'''n=1
while n<=10:
    print(n*n)
    n+=1'''

#printing the elemnts from the give list
'''list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1'''

#search for a number x in the tuple using loop: (USING BREAK KEYWORD)
'''t=(1,4,9,16,25,36,49,64,81,100)
x= int(input("Enter Number :"))
i=0

while i<len(t):
    if (t[i]==x):
        print('Found at',i)
        break
    else:
        print('Finding..')
    i+=1'''

#USING CONTINUE KEYWORD
'''i=0
while i<=5:
    if (i==4):
        i+=1
        continue #skip
    print(i)
    i+=1'''

#FOR LOOPs
for j in range(5):
    for i in range(j):
        print(i,end="")
    print()

'''str="Yashi Tiwari"

for value in str:
    if(value=='i'):
        print(value,'i found')
        break
    print(value)
print('Loop Ended')
'''

#Practice Questions
#ques.1
'''list1=[1,4,9,16,25,36,49,64,81,100]
for value in list1:
    print(value)'''
#ques.2
'''tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input('x:'))

for int in tuple:
    if(int==x):
        print("Found")
        break
    print(int)
   '''
#Practice problems
#WAP to find the sum of first n numbers.
#FOR LOOP
'''n=5
sum=0
for i in range(n+1):
    sum+=i
print(sum)'''
#WHILE LOOP
'''n=5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)'''

#WAP to find the factorial of first n numbers
'''n=5
fac=1
for i in range(1,n+1):
    fac*=i
print('Factorial',fac)'''

#Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
'''n=int(input('enter num:'))
sum=0
while n>0:
    if (n<0):
        print(sum)
        sum+=n
        break
    n=int(input('Enter Number:'))'''
    

#Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done


#name=input('Name:')
#while name!= 'End':
#     name = input ('Other Name:')
#print('I am done')

# a = []
# def get_permutations(string, i = 0):

#     if i == len(string):
#        a.append("".join(string))

#     for j in range(i, len(string)):

#             words = [c for c in string]
#             words[i], words[j] = words[j], words[i]

#             get_permutations(words, i + 1)

# get_permutations("Timur")


# i = 1
# t = int(input())
# while i<=t:
#     n = int(input()) #length
#     i += 1
#     s = input()
#     if(len(s)==n and s in a):
#         print("YES")
#     else:
#         print("NO")