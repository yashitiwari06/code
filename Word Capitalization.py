str=input()
if (len(str)<=10**3):
    a=str[0]
    b=str[1:]
    capital=a.capitalize()
    print(capital+b)
else:
    print(None)
    