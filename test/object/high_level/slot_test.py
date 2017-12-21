import functools
from types import MethodType


from test.object.class_test import Student

s = Student("ZXC", 12, "MALE", **{"语文": 100})
s1 = Student("ZXC", 12, "MALE", **{"语文": 100})


def do_homework():
    print("学生需要做作业")


s.do_homework = do_homework

s.do_homework()

s.print_info()


def set_country(self, country):
    self.country = country


def get_country(self) :
    return self.country


Student.set_country = set_country

Student.get_country = get_country


def set_age(self, age):
    self.__age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.__age)
# print(s1.__age)
s.print_info()

s.set_country("China")
s1.set_country("Australia")

print(s.get_country())
print(s1.get_country())