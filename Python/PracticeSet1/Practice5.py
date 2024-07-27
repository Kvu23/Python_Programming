# this programs explains global and local variable concepts

msg = "awesome"

def myfunc():
    print("Global variable concepts")
    print("python is " + msg)

def myfunc1():
    msg = "fantastic"
    print("local variable concepts")
    print("python is "+ msg)

myfunc()
myfunc1()

