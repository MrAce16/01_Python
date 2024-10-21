def my_decorater(func):
    def wrapper():
        print("Running", func.__name__)
        func()
        print("complete")
    return wrapper


@my_decorater
def do_this():
    print("Doing this")


@my_decorater
def do_that():
    print("Do that")


do_this()
do_that()

# o/p -->
