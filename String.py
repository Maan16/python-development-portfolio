#Normal String
first= 'John'
last= "Smith"
'I want to print thye exact below'
'John [Smith] is a coder'
message=  first   + ' [' + last + '] is a coder'
print(message)

''' While the above approach perfectly works but when we have large
number of string text it will be difficult to do it that way so we need
different approach and that is called Formated string '''

#Foramted String
msg= f'{first} [{last}] is a coder'
print(msg)


# More Strings

course= 'I am learning Python'
print(len(course)) # print and length (len) are general purpose function not specific to something

print(course.upper())  #this is a methode as this belongs to specific function
print(course.lower())  #this is a methode as this belongs to specific function
print(course.find('e'))  #this is a methode as this belongs to specific function
print(course.replace('e', 's'))  #this is a methode as this belongs to specific function

print('Python' in course)






