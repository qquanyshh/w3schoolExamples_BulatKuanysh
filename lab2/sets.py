'''
Python Sets
'''
#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#7
set1 = {"abc", 34, True, 40, "male"}

#8
myset = {"apple", "banana", "cherry"}
print(type(myset))

#9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


'''
Python - Access Set Items
'''
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

'''
Python - Add Set Items
'''
#1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

'''
Python - Remove Set Items
'''
#1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

'''
Python - Loop Sets
'''
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


'''
Python - Join Sets
'''
#1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#7
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
