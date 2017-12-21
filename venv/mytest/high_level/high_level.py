import os

for i in [i * i for i in range(10)]:
    print(i)

for pj in [m + n for m in "ABC" for n in "ZXC"]:
    print(pj)

for d in os.listdir("."):
    print(d)

for k, v in {"name": "ZXC", "age": 22}.items():
    print(k, ":", v);

dict = ["ZXC", "ZXM", "XCG"]
for i, v in enumerate(dict):
    print(i, ":", v)

print(dict)
print(enumerate(dict))

print(enumerate({"name": "ZXC", "age": 22}))

for k in enumerate({"name": "ZXC", "age": 22}):
    print(k[-1 ])
