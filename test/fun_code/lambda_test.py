fun1 = lambda x,y : x + y
print(fun1(5,6))

def build(x, y) :
    return lambda :x * x + y * y

f = build(1,2)
print(f())