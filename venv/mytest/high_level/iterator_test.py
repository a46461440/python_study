from collections import Iterable

print(isinstance(100, Iterable))
print(isinstance("100", Iterable))
iterator1 = (x for x in "100")
iterator2 = iter(list(iter("321")))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

while True :
    try :
        print(next(iterator2))
    except Exception :
        break

print("顺利执行到这里")

