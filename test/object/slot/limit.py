class Limit:
    __slots__ = 'key', 'value'


limit = Limit()


def set_key(self, key):
    self.key = key


def set_value(self, value):
    self.value = value


Limit.set_key = set_key
Limit.set_value = set_value

limit.set_key("Name")
limit.set_value("ZXC")
print(limit.key)
print(limit.value)
