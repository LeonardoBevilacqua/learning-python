# Data types
x = "Hello World"
print(x, type(x)) # str
x = 20
print(x, type(x)) # int
x = 20.5
print(x, type(x)) # float
x = 1j
print(x, type(x)) # complex
x = ["Apple", "Banana", "cherry"]
print(x, type(x)) # list
x = ("Apple", "Banana", "cherry")
print(x, type(x)) # tuple
x = range(6)
print(x, type(x)) # range
x = {"name": "Leonardo", "age": 26}
print(x, type(x)) # dict
x = {"Apple", "Banana", "cherry"}
print(x, type(x)) # set
x = frozenset({"Apple", "Banana", "cherry"})
print(x, type(x)) # frozenset
x = True
print(x, type(x)) # bool
x = b"Hello"
print(x, type(x)) # bytes
x = bytearray(5)
print(x, type(x)) # bytearray
x = memoryview(bytes(5))
print(x, type(x)) # memoryview
x = None
print(x, type(x)) # None