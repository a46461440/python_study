def lazy_sum(arg) :
    def sum() :
        sum_real  = 0
        for per in arg :
            sum_real = sum_real + per
        return sum_real
    return sum

list1 = [1,2,3,4,5,6]
f = lazy_sum(list1)()
print(f)
print(f)


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs

f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)