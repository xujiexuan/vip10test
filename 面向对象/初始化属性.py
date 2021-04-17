class Washer(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wash(self, haha):
        print(f'我会洗衣服{haha}{self.width},{self.height}')

    def __str__(self):
        return '这是洗⾐机的说明书'

    def __del__(self):
        print(f'{self}对象已经被删除')


haier1 = Washer(500, 800)

haier1.wash('再见')
print(f'{haier1.width},{haier1.height}')
print(haier1)
del haier1