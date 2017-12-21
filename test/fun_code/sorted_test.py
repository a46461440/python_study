list1 = [26,5,-1,-16,2,21]

print(sorted(list1, key=abs))

list2 = ["CXZ","ZXC","zxc","abc"]
print(sorted(list2, key=str.lower))

print(sorted(list2, key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_cacu (*ele) :
    for k,v in ele:
        # return str(k).upper()
        return int(v)
print(sorted(L, key=sort_cacu))