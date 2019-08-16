class CheckMeta(type):
    def __new__(mcs, *args, **kwargs):
        name, bases, namespace = args

        if (not namespace.get("Meta", None)) and (bases != ()):
            raise Exception("Can not configure class. Meta is missing")

        r = super().__new__(mcs, *args, **kwargs)

        return r


class Model(metaclass=CheckMeta):
    pass


class UserModel(Model):
    class MegaNotMeta:  # Not Meta
        fields = ['name', 'email', 'birth_date']


# expect Exception: Can not configure class. Meta is missing
