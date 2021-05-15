class Dog(object):
    __tooth = 10

    @classmethod
    def get__tooth(cls):
        return cls.__tooth

    @classmethod
    def set__tooth(cls, n):
        cls.__tooth = n
       