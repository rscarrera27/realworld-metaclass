class DisallowMultipleInheritance(type):
    def __new__(mcs, *args, **kwargs):
        if len(args[1]) > 1:  # if base class tuple has more than one elements, raise exception
            raise Exception(f"Can't be subclassed with multiple inheritance: {args[1]}")
        r = super().__new__(mcs, *args, **kwargs)
        return r


class Foo(metaclass=DisallowMultipleInheritance):
    pass


class Bar:
    pass


class Zee(Foo, Bar):
    pass


# Expected results: 
# Exception: Can't be subclassed with multiple inheritance: (<class '__main__.Bar'>, <class '__main__.Foo'>)
