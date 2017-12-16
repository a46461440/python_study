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
