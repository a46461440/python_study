import time

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]
list2 = ["",None,"ZXC","   ","ZXM"]

def filter1(arg) :
    return arg % 3 == 1

print(list(filter(filter1, list1)))

def filter2(arg) :
    return arg and arg.strip()

print(list(filter(filter2, list2)))

# 求素数
def is_not_su (num) :
    cacu = 2;
    if num < 4 :
        return False
    while cacu < num :
        if num % cacu == 0 :
            return False
        cacu  = cacu + 1
    return True

def is_odd (num) :
    return num % 2 == 1

list3 = (x for x in "1000")
start = time.time()
print(list(filter(is_not_su, filter(is_odd,range(10)))))
time1 = time.time() - start
start = time.time()
print(list(filter(is_not_su, range(10))))
time2 = time.time() - start
print(time1 ,":", time2)