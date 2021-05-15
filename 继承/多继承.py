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
class Prentice(Master,School):
    def __init__(self):
        self.kongfu = '[自创煎饼果子配方]'

    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 3.创建对象xiaoming
xiaoming = Prentice()
# 4.对象访问实例化属性
# print(xiaoming.kongfu)
# 5.对象调用实例化方法
# xiaoming.make_cake()
# xiaoming.make_master_cake()
# xiaoming.make_school_cake()

class TuSun(Prentice):
    pass

xiaogang = TuSun()
# 4.对象访问实例化属性
# print(xiaoming.kongfu)
# 5.对象调用实例化方法
# xiaogang.make_cake()
# xiaogang.make_master_cake()
# xiaogang.make_school_cake()
# xiaogang.make_cake()