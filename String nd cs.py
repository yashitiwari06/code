'''
str="Hi I'm Yashi Tiwari.\nI am a coder."
print(str)
'''
#Concatenation
'''
str1='Yashi'
str2="Tiwari"
print(str1+str2)
'''
#SLICING
'''
str='yashi tiwari'
print(str[0:5])'''

#For access the string till the last index 
#Option1
'''str='yashi tiwari'
print(str[6:12])'''
#option2
'''str='yashi tiwari'
print(str[6:])'''

#For access the string from the 0 index
#option1
'''str='nice_team'
print(str[0:5])'''
#option2
'''str='nice_team'
print(str[:5])'''

#STRING FUNCTIONS
'''str1='hi, I am a coder.'
print(str1.endswith('der.')) #returns true or false
print(str1.capitalize()) 
print(str1.replace('i','e'))
print(str1.find('I')) #returns indexing
print(str1.count('a'))#returns the no. of occurence of the entred string'''

#wap to input the user's first name & print it's length
'''Name=input('Enter ur first name:')
print(len(Name))'''

#wap to find the occurence of $ in a string
#s='Transfer $1000 to my account'
#print(s.count('$'))

#NESTING
#SUPPOSE DRIVING AGE LIMIT IS 18-80
'''age=int(input('age:'))
if(age>=18):
    if(age>80):
        print('Cannot Drive')
    else:
        print('Can Drive')
else:
    print('Cannot Drive')'''

#wap to find the greatest of 3 numbers entered by the user
'''
a=int(input('1st Num:'))
b=int(input('2nd Num:'))
c=int(input('3rd Num:'))
if (a>=b and a>=c):
    print(a)
elif (b>=a and b>=c):
    print(b)
else:
    print(c)'''
#wap to find the greatest of 4 numbers entered by the user
'''
a=int(input('1st Num:'))
b=int(input('2nd Num:'))
c=int(input('3rd Num:'))
d=int(input('4th Num:'))
if ((a>=b and a>=c) and a>=d):
    print('greatest num:',a)
elif ((b>=a and b>=c) and b>=d):
    print('greatest num:',b)
elif ((c>=a and c>=b) and c>=d):
    print('greatest num:',c)
else:
    print('greatest num:',d)
'''