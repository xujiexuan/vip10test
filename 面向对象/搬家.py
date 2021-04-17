"""
功能描述：
编写人：
编写日期：
实现逻辑：


"""


class FangZi(object):
    def __init__(self, mingcheng, mianji):
        self.mingcheng = mingcheng
        self.mianji = mianji
        self.shengyumianji = mianji
        self.jiajuliebiao = []

    def FangJiaJu(self, jiaju):
        self.jiajuliebiao.append(jiaju.mingcheng)
        if self.shengyumianji >= jiaju.mianji:
            self.shengyumianji = self.shengyumianji - jiaju.mianji
        else:
            return 0

    def __str__(self):
        return f'{self.mingcheng},{self.mianji},{self.shengyumianji},{self.jiajuliebiao}'


class JiaJu(object):
    def __init__(self, mingcheng, mianji):
        self.mingcheng = mingcheng
        self.mianji = mianji


fangzi1 = FangZi("haha", 500)
JiaJu1 = JiaJu("yizi", 50)
for i in range(0, 101):
    fangzi1.FangJiaJu(JiaJu1)
    if fangzi1.FangJiaJu(JiaJu1) == 0:
        print('再见')
        break
print(fangzi1)
