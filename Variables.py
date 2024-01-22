'''
Python Variables
'''

#1
x = 5
y = "John"
print(x)
print(y)


#22
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


#333
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#4444
x = 5
y = "John"
print(type(x))
print(type(y))


#55555
x = "John"
# is the same as
x = 'John'


#666666
a = 4
A = "Sally"
#A will not overwrite a


'''
Variable Names
'''

#1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#22
#Camel Case : Each word, except the first, starts with a capital letter.
myVariableName = "John"


#333
#Pascal Case : Each word starts with a capital letter.
MyVariableName = "John"

#4444
#Snake Case : Each word is separated by an underscore character.
my_variable_name = "John"


'''
Assign Multiple Values
'''


#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#22
x = y = z = "Orange"
print(x)
print(y)
print(z)


#333
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


'''
Output Variables
'''


#1
x = "Python is awesome"
print(x)


#22
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


#333
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#4444
x = 5
y = 10
print(x + y)


#55555
x = 5
y = "John"
print(x, y)


'''
Global Variables
'''


#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#22
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#333
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#4444
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)