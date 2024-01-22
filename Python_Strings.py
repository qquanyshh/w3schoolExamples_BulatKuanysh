'''
Python Strings
'''

#1
print("Hello")
print('Hello')


#22
a = "Hello"
print(a)


#333
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#4444
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#55555
a = "Hello, World!"
print(a[1])


#666666
for x in "banana":
  print(x)


#7777777
a = "Hello, World!"
print(len(a))


#88888888
txt = "The best things in life are free!"
print("free" in txt)


#999999999
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#0000000000
txt = "The best things in life are free!"
print("expensive" not in txt)


#10
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


'''
Python - Slicing Strings
'''

#1
b = "Hello, World!"
print(b[2:5])


#22
b = "Hello, World!"
print(b[:5])


#333
b = "Hello, World!"
print(b[2:])


#4444
b = "Hello, World!"
print(b[-5:-2])


'''
Python - Modify Strings
'''

#1
a = "Hello, World!"
print(a.upper())


#22
a = "Hello, World!"
print(a.lower())


#333
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#4444
a = "Hello, World!"
print(a.replace("H", "J"))


#55555
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


'''
Python - String Concatenation
'''

#1
a = "Hello"
b = "World"
c = a + b
print(c)


#22
a = "Hello"
b = "World"
c = a + " " + b
print(c)


'''
Python - Format - Strings
'''

#1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#22
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#333
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


'''
Python - Escape Characters
'''

#1
txt = "We are the so-called \"Vikings\" from the north."