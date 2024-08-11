'''count=1
while count <=10:
    print(count)
    count+=1'''


'''for i in range(1,10):
    if (i%2==0):
        print(i)'''

#let say given number is 10
'''sum=0
for i in range(11):
    sum+=i
print(sum)
   '''

#let say the range is from 1 to 10
'''sum=0
for i in range(1,11):
    if (i%2!=0):
        sum+=i
print(sum)
print('LOOP ENDED')
'''

#let say the given number is 10
#USING FOR LOOP
'''product=10
for i in range(1,11):
    print(i*10)'''

#USING WHILE LOOP
'''count=1
while count<=10:
    print(count*5)
    count+=1'''

'''x=int(input("X Coodinate of friend's House: "))
a=x/5
b=(x/5)+1
a=int(a)
b=int(b)
if(x==1):
    print("Minimum No. of Steps:",1)
elif(x==2):
    print("Minimum No. of Steps:",1)
elif(x==3):
    print("Minimum No. of Steps:",1)
elif(x==4):
    print("Minimum No. of Steps:",1)
elif(x==5):
    print("Minimum No. of Steps:",1)
elif(x%5==0):
    print("Minimum No. of steps:",a)
else:
    print("Minimum No. of steps:",b)'''

'''x=int(input("X Coodinate of friend's House: "))
a=x/5
b=(x/5)+1
a=int(a)
b=int(b)
if(x==1 or x==2 or x==3 or x==4 or x==5):
    print("Minimum No. of Steps:",1)
elif(x%5==0):
    print("Minimum No. of steps:",a)
else:
    print("Minimum No. of steps:",b)'''

'''t=int(input())
count=1
while count<=t:
    str=input()
    if (len(str)==3 and str=="YES" or str=="YEs" or str=="Yes" or str=="yes" or str=="yES" or str=="yEs" or str=="yeS" or str=="YeS"):
            print("YES")
    else:
            print("NO")'''

#a, b=[int(a) for a in input().split()]
#print(a,b)

n=int(input())
