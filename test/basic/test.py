print("你好");
print("I\'am a \"superman\"", "," , "Yes,", r'\\\t\\', r'\\\t\\');
print("周润明的Unicode:", ord("周"), ord("润"), ord("明"));
print(chr(21608), chr(28070), chr(26126));
encode = "周润明".encode("utf-16");
print(encode.decode("utf-8", errors='ignore'));
while False:
    name = input("please enter your name:");
    if len(name) >= 2:
        print("OK");
    else:
        print("NO");
print('Hello,%s ,you have $%d' %('ZXC',123));
print('Hello,{0} ,you have ${1:.2f}'.format('ZXC',123));

list = ["ZXC", "WYL"];
list.append("ZHY");
list.insert(1, 6);
print(list);
print(len(list));
list.pop(1);
print(len(list));
if False:
    print("No");
elif True:
    print("No2");
else:
    print("OK");
    print("OK2");
print("Yes");
age = input("输入年龄");
age = int(age);
print(age-18);