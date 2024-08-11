#Pattern 1
''' 
****
**** 
****
****
'''

'''for i in range(1,5):
    
    for j in range(1,5): # to print leading spaces 
        print(" ",end="")
        
    for k in range(1,5): #to print the symbol in current rows
        print("*", end="")
    print()'''

#Patterns 2

'''for i in range(1,6):

    for j in range(1,6):
        print(" ", end = "")

    for k in range(1, i+1):
        print(k,end="")
        
    print()

  '''

#Pattern 3
'''for i in range(1,6):

    for j in range(1,6):
        print(" ", end="")
    for k in range (1,i+1):
        print(i,end="")
    print()
    '''

#Pattern 4

#key concept Total row - row no - 1
'''for i in range(1,6):

    for j in range(1,6):
        print(" ",end ="")
    for k in range(5-i+1):
        print("*",end ="")
    print()
'''

# pattern 5 (DOUBT)

'''for i in range(1,6):

    for k in range(5-i+1):
        print(k+1,end ="")
    print()
'''
#Pattern 6 (Pyramid) [space,star,space]
'''for i in range(1,6):
    
    for j in range(5 - i):
        print(" ",end ="")
    for k in range((2*i) - 1):
        print("*",end ="")
    for l in range(5 - i):
        print(" ",end ="")
    print()'''

#Pattern 7

'''for i in range(5):
    
    for j in range(i):
        print(" ",end ="")
    for k in range(10-(2*i+1)):
        print("*",end ="")
    for l in range(i):
        print(" ",end ="")
    print()'''

#Pattern 8 = Pattern 7 + pattern 6

#pattern 9

'''
for i in range(1,6):

    for j in range(i):
        print("*",end = "")
    print()
    

for k in range(1,5):

    for l in range(5-k):
        print("*",end = "")
    print()'''

#Pattern 11

'''for i in range(1,6):
    
    for j in range(i):
        if(i % 2 == 0):
            if(j % 2 == 0):
                print(1,end = " ")
            else:
                print(0,end = " ")
        else:     
            if(j % 2 == 0):
                print(0,end = " ")
            else:
                print(1,end = " ")
       
    print()'''



#Pattern 12
'''for i in range(4):

    for j in range(i+1):
        print(j + 1,end = "")

    for k in range(6-(2*i)):
        print(" ",end = "")

    for l in range(i+1):
        print(i + 1 - (l),end = "")
    print()

    '''

#Pattern 13
'''count = 1
for i in range(5):
   
    for j in range(i + 1):
        print(count,end = " ")
        count += 1
    print()'''

#Pattern 14
'''for i in range(6):
    count = 'A'
    for j in range(i):
        print(count,end = " ")
        count = chr(ord(count) + 1)
    print()'''


#Pattern 15
'''for i in range(5):
    count = 'A'
    for j in range(5 - i):
        print(count, end =" ")
        count = chr(ord(count) + 1)
    print()
 '''
 #Pattern 16
'''count = "A"
for i in range(5):

    for j in range(i + 1):
        print(count,end = "  ")
    count = chr(ord(count) + 1)
    print()'''

#Pattern 17
'''for i in range(4):

    count = "A"
    for j in range(4-(i + 1)):
        print(" ", end = " ")
        

    for j in range(2*i + 1):
        if(j<(i)):
            print(count ,  end = " ")
            count = chr(ord(count)+1)
        else:
            print(count ,  end = " ")
            count = chr(ord(count)-1)
    
    for l in range(4 - (i + 1)):
        print(" ", end = " ")

    print()'''

#Pattern 18
'''for i in range(5):

    for j in range(5-i):
        print("*",end = "")
    for k in range(2*i):
        print(" ",end = "")
    for l in range(5-i):
        print("*",end = "")
    print()

for r in range(5):

    for o in range(r+1):
        print("*",end = "")
    for u in range(8-((2*r))): # instead of 8 we can write 2*n - 2 n=5
        print(" ",end = "")
    for t in range(r+1):
        print("*",end = "")
    print()'''

#Pattern 19(doubt)
'''ch = "E"
for i in range(5):
    for j in range(i + 1):
       print(ch,end = " ")
       ch = chr(ord(ch) + 1)
    ch = chr(ord(ch) - (i+2))
    print() '''

'''ch = "E"
for i in range(5):
    temp = ch
    for i in range(i + 1):
        print(temp, end = " ")
        temp = chr(ord(temp) - 1)
    
    print()'''

'''
1  E
2  D E
3  C D E 
4  B C D E
5  A B C D E'''
#Pattern 20
'''for r in range(5):

    for o in range(r+1):
        print("*",end = "")
    for u in range(8-((2*r))): # instead of 8 we can write 2*n - 2 n=5
        print(" ",end = "")
    for t in range(r+1):
        print("*",end = "")
    print()

for i in range(1,5):

    for j in range(5-i):
        print("*",end = "")
    for k in range(2*i):
        print(" ",end = "")
    for l in range(5-i):
        print("*",end = "")
    print()'''

#Pattern 21
'''for i in range(2):

    for j in range(2 - i):
        print("*",end = "")
    for k in range(2 * i):
        print(" ", end = "")
    for l in range(2 - i):
        print("*", end = "")
    print()

for y in range(2):

    for t in range(y + 1):
        print("*", end = "")
    for h in range(2-(2*y)):
        print(" ", end = "")
    for n in range(y + 1):
        print("*", end = "")   
    print()'''

#Pattern 22