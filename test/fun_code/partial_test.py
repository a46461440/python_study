import functools


def fun1(age, name):
    if age < 18:
        print("{0}是年轻人".format(name))
    else:
        print("%s是老年人" % (name))
    pass


fun = functools.partial(fun1, name="ZXC")

print(fun(171))

print(functools.__all__[0])

