class Student(object):

    __static__ = []

    country = ""

    def __init__(self, name, age, sex, **score):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__score = score

    def print_info(self):
        for k,v in self.__score.items():
            print("%s(%s)现在%d岁,%s得分%s" % (self.__name, self.__sex, self.__age, k, v))
