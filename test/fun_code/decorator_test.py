import functools


def log(fun) :
    def wrapper (*args , **kw) :
        print("function %s 被调用" % (fun.__name__))
        return fun(*args, **kw)
    return wrapper


@log
def caculate_add(x, y) :
    return x + y

print(caculate_add(1,2))

def log(text) :
    def decorator(fun) :
        @functools.wraps(fun)
        def wrapper (*args , **kw) :
            print("%s function %s 被调用" % (text, fun.__name__))
            return fun(*args, **kw)
        return wrapper
    return decorator


@log("execute")
def caculate_add(x, y) :
    return x + y

print(caculate_add(1,2))