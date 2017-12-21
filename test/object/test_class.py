from functools import reduce

from test.object.class_test import Student


def sorted_by_score(ele):
    print(ele)
    return ele[1]


L = dict(sorted({"外语": 90, "数学": 80, "语文": 60}.items(), key=sorted_by_score, reverse=True))
student = Student("ZXC", 22, "MALE", **L)
student2 = Student("ZXC", 22, "MALE", **L)
# student3 = student.__init__("ZXM", 23, "FEMALE", **L)
student.print_info()
student.__name = "我"
print(student._Student__name)
print(student.__name)
print("----------------------------------------")
student.__static__.append("Z")
student2.__static__.append("X")
Student.__static__.append("C")
print(reduce(lambda x, y: x + y, student.__static__))
