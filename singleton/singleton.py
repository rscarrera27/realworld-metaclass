class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class C(metaclass=Singleton):
    pass


if __name__ == "__main__":
    a = C()
    b = C()

    print(a is b)  # Expected 'True' because Singleton metaclass returns same object

