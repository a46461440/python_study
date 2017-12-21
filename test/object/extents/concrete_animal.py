from test.object.extents.animal import Animal


class Dog(Animal):
    def run(self):
        print("dog is running")


class Cat(Animal):
    def run(self):
        print("cat is running")


dog = Dog()
cat = Cat()

cat.run_twice()
dog.run_twice()

print(isinstance(cat, (list, tuple, Animal)))
try:
    getattr(cat, "run2")()
except Exception:
    pass
