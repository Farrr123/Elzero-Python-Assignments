from functools import wraps

# Generator Example

# my_string = "Elzero"


# def reverse_string(my_string):
#     for char in my_string[::-1]:  # noqa: UP028
#         yield char


# for char in reverse_string("Elzero"):
#     print(char)


# Decorator Example


def decoration(func):
    @wraps(func)
    def wrapper():
        print("Sugar Added From Decorators")
        func()
        print("####################")

    return wrapper


@decoration
def make_tea():
    print("Tea Created")


@decoration
def make_coffee():
    print("Coffee Created")


make_tea()
make_coffee()
