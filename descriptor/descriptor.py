"""
Implementation based on PEP-484. some details are excluded for a easy reading
"""


class Meta(type):
    def __new__(mcs, *args, **kwargs):
        name, bases, namespace = args

        self = super().__new__(mcs, name, bases, namespace)

        for k, v in self.__dict__.items():
            func = getattr(v, '__set_name__', None)
            if func is not None:  # trigger hook if exists
                func(self, k)

        return self


class Desc:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class C(metaclass=Meta):
    v = Desc()


if __name__ == "__main__":
    c = C()

    c.v = 3
    print(c.v == 3)  # Expected True, Meta call set_name hook

