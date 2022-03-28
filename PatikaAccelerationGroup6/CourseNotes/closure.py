def outer1():
    msg = "Hey"
    def inner():
        print(msg)
    return inner()              # Returns result of the inner function

print("-------------Example 1---------------")
outer1()
print("Example1 : ", outer1())  # Outer1() --> Returns: Inner(), Inner() --> Returns : None

def outer2():
    msg = "Hey"
    def inner():
        print(msg)
    return inner                # Returns reference of the inner function

print("-------------Example 2---------------")
f = outer2()
f()
print("Example2 : ",f())        # Outer2() --> Returns: inner reference into f,  f() --> Returns : None

def outer3(msg):
    msg = msg
    def inner():
        print(msg)
    return inner                # Returns reference of the inner function

print("-------------Example 3---------------")
hi_f = outer3("hi")             # outer3("hi") --> Returns: inner reference into hi_f, hi_f() --> Returns : None
hey_f = outer3("hey")           # outer3("hey") --> Returns: inner reference into hey_f, hey_f() --> Returns : None

hi_f()
hey_f()
print("Example3 : ",hi_f())