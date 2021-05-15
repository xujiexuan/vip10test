# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[五香煎饼果子配方]'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[香辣煎饼果子配方]'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')


# 2.徒弟类
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[自创煎饼果子配方]'
        self.__money = 2000000

    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money = 500

    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class TuSun(Prentice):
    pass


xiaoming = Prentice()
xiaogang = TuSun()
# print(xiaoming.__money)
# print(xiaogang.__money)
print(xiaogang.get_money())
xiaogang.set_money()
print(xiaogang.get_money())
