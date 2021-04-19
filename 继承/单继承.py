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
class Prentice(Master):
    pass


# 3.创建对象xiaoming
xiaoming = Prentice()
# 4.对象访问实例化属性
print(xiaoming.kongfu)
# 5.对象调用实例化方法
xiaoming.make_cake()
