x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)

myFunc()

print("Python is " + x)

def myFuncGlobal():
    global y
    y = "great"

myFuncGlobal()
print("Python is " + y)