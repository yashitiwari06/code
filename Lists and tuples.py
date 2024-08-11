'''Marks=[1,2,3,4,5]
print(Marks[3])
print(len(Marks))'''

#List Functions
'''list=[1,2,3,0,5]
list.append(7)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(8,45) #here 8 is the index and 45 is the element to be added on that indexing
print(list)'''

#TUPLE FUNCTIONS
'''t=(1,2,3,4,4)
print(t.index(4)) # here we have entered the element and it returns the index of that element
print(t.count(4)) # 4 is the element '''

#wap to ask the user to enter names of their 3 favorite movies Z& store them in list
'''
a=input('1st fav movie:')
b=input('2nd fav movie:')
c=input('3rd fav movie:')
fav_movies=[a,b,c]
print(fav_movies)'''

#WAP to check if a list contains a palindrome of elements 
'''list2=[1,2,1]
list1=[5,6,7]

list_copy1=list1.copy()
list_copy1.reverse()

if(list_copy1==list1):
    print('yes')
else:
    print('NO')'''

#WAP to count the number of students with grade A in the following tuple
t=('C','D','A','A','B','B','A')
print(t.count('A'))

# WAP to create a list and sort them
l=['C','D','A','A','B','B','A']
l.sort()
print("Sorted List: ",l)