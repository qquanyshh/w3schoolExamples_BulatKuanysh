#1
print(10 > 9)
print(10 == 9)
print(10 < 9)


#22
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#333
print(bool("Hello"))
print(bool(15))


#4444
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#55555
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#666666
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#7777777
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#88888888
def myFunction() :
  return True

print(myFunction())

#999999999
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#0000000000
x = 200
print(isinstance(x, int))