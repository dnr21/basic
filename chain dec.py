def star(func):
    def inner(*args, **kwargs):
        print("*" * 20)
        func(*args, **kwargs)
        print("*" * 20)
    return inner
def percent(func):
    def inner(*args, **kwargs):
        print("%" * 20)
        func(*args, **kwargs)
        print("%" * 20)
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer("decaration")
