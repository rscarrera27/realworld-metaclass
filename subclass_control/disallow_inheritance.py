class DisallowInheritance(type):
    def __new__(mcs, *args, **kwargs):
        cls = [c for c in args[1] if isinstance(c, mcs)]
        if args[1]:
            raise Exception(f"Can't subclass this classes: {cls}")
        r = super().__new__(mcs, *args, **kwargs)
        return r


class Foo(metaclass=DisallowInheritance):
    pass


class Bar(Foo):
    pass

# Expected results:
# Exception: Can't subclass this classes: [<class '__main__.Foo'>]
