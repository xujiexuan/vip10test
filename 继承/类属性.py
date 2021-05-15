class Dog(object):
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

Dog.tooth = 12
print(wangcai.tooth)
print(xiaohei.tooth)