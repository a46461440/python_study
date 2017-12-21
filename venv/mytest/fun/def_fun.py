import cmath


def my_caculate(x, y, symbol) -> (float, int):
    if symbol not in ('+', '-', '*', '/'):
        return cmath.cos(x), cmath.sin(y);
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return;
    if symbol == '+':
        return x + y;
    elif symbol == '-':
        return x - y;
    elif symbol == '*':
        return x * y;
    elif symbol == '/':
        return x / y;


def my_multiplication(x, n=2) -> int:
    s = 1;
    while n > 0:
        s = s * x;
        n = n - 1;
    return s;


def get_info(name, sex, age=6, city="ChangSha"):
    print(name, ":", sex, ":", age, ":", city);


print(my_caculate(1, 2.1, 'w'));

print(my_multiplication(3));
print(my_multiplication(3, 3));

print(get_info("ZXC", "MALE", 22));
print(get_info("ZXC", "MALE", city="ShenZhen"));


def change_param(name, *arr):
    for sing in arr:
        print(name, ":", sing);


change_param('ZXC', 1, 2, 3, 4, 5, 6, 7, 8, )

other = {'city': "ChangeSha", 'job': "Engineer"};

print("-----------------------------------")


# 用**other来接受变长的dict 全部会被转换成dict
def person(name, age, **other):
    print(name, ":", age, ":other:", other);
    print(other.items());


person("ZXC", 23, **other);


def person(name, age, *, city, job):
    print(name, ":", age, ":", city, ":", job);


person("ZXC", 22, city="ChangSha", job="Engineer");


def person(name, age, *args, city, job):
    print(name, ":", args, age, ":", city, ":", job);


person("ZXC", 22, "OK", city="ChangSha", job="Enginner");

print(other);

other = ["ZXC", "ZXM", "XCG"];
print(other[0:1]);
print(other[1:][::2]);
