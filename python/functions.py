# Functions start with def
def my_function():
    print("Hello from a function")

my_function()

def another(a, b):
    print("My favorite color is " + a)
    print("My home state is " + b)

another("red", "Ohio")

def my_home(state = "Ohio"): # With a default value that can be overridden
    print("I grew up in " + state)

my_home()
my_home("Indiana")
my_home("Tennessee")

def some_math(a, b):
    return a + b    # return - a more common tool than print()

print(some_math(3, 6))

x = lambda a, b : a + b # same as above but in a small anon function
print(x(33, 44))
    
# Recursion
def recurse_me(n):
    if n > 0:
        print(n)
        n = recurse_me(n - 1)
    else:
        print(n)
        print("fini")

recurse_me(11)

