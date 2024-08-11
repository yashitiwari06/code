x=int(input())
a=x/5
b=(x/5)+1
a=int(a)
b=int(b)
if(x==1 or x==2 or x==3 or x==4 or x==5):
    print(1)
elif(x%5==0):
    print(a)
else:
    print(b)