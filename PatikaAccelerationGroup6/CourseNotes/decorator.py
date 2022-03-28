"""
def print_func():
    print("Hey!")

def decorator_func(func):                       #   decorator_func() --> Takes "func" as INPUT 
    def wrapper_func():                         #   wrapper_func() --> Does not take INPUT
        return func()                           #   wrapper_func() --> RETURNS the execution of "func()"

    return wrapper_func                         #   decorator_func() --> RETURNS the reference of "wrapper_func"

decorated_print = decorator_func(print_func)    #   Executes the "decorator_func" with the reference of "print_func" as INPUT
                                                #   RETURNS the result into the "decorated_print"
decorated_print()                               #   Executes the "decorated_print
"""

#################################################
"""
def print_func():
    print("Hey!")

def decorator_func(func):                       #   decorator_func() --> Takes "func" as INPUT 
    def wrapper_func():                         #   wrapper_func() --> Does not take INPUT
        print(f"The name of the function is {func.__name__}")
        return func()                           #   wrapper_func() --> RETURNS the execution of "func()"

    return wrapper_func                         #   decorator_func() --> RETURNS the reference of "wrapper_func"

decorated_print = decorator_func(print_func)    #   Executes the "decorator_func" with the reference of "print_func" as INPUT
                                                #   RETURNS the result into the "decorated_print"
decorated_print()                               #   Executes the "decorated_print"
"""

#################################################
"""
def decorator_func(func):                       #   decorator_func() --> Takes "func" as INPUT 
    def wrapper_func():                         #   wrapper_func() --> Does not take INPUT
        print(f"The name of the function is {func.__name__}")
        return func()                           #   wrapper_func() --> RETURNS the execution of "func()"

    return wrapper_func                         #   decorator_func() --> RETURNS the reference of "wrapper_func"

@decorator_func                                 #   decorated_print = decorator_func(print_func) ifadesinin kısayolu
def print_func():
    print("Hey!")

print_func()                                    #   decorated_print() yerine artık print_func() kullanılır
"""
#################################################
"""
def func(name, number):
    print(f"Name: {name}, number: {number}")

func("Jack", 102)
"""
#################################################

def decorator_func(func):
    def wrapper_func(*args):
        print(f"The name of the function is {func.__name__}")
        return func(*args)
    return wrapper_func

@decorator_func
def func(name, number):
    print(f"Name: {name}, number: {number}")

func("Jack", 102)