from functools import reduce


def fun1(x) :
    return x ** 2

list1 = [1,2,3,4,5,6,7,8,9,10]

one = map(fun1, list1)
print(list(one))
print("----------------------------------------")
for y in (x*x for x in list1) :
    print(y)

def fun2 (x, y) :
    return x + y

two = reduce(fun2, list1[:3])
print(two)

result = reduce(fun2, map(str, list1))
print(result)
print(isinstance(result, str))

def fun3(x,y) :
    return x * 10 + y

three = reduce(fun3, list1)
print(three)
print(isinstance(three, str))

def practice(input) :
    if isinstance(input, str) :
        return str(input[:1]).upper()+str(input[1:]).lower()

names = ["jAMEs", "ZXC", "WYL"]
print(list(map(practice, names)))