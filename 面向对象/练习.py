"""
功能描述：定义一个老师类，老师有姓名和性别，还有交的课程，可以教学，实现：xx老师，性别是xxx。教xxx课
编写人：
编写日期：
实现逻辑：


"""


class LaoShi(object):
    def __init__(self, xingming, xingbie, kecheng):
        self.xingming = xingming
        self.xingbie = xingbie
        self.kecheng = kecheng

    def jiaoKe(self):
        print(f'我在教课{self.kecheng}')


laoshi1 = LaoShi("haha", "nv", "yuwen")

laoshi1.jiaoKe()
print(f'{laoshi1.xingming},{laoshi1.xingbie},{laoshi1.kecheng}')
