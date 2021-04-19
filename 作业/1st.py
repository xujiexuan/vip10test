# 前提：课上的所有内容复习一遍，检查哪些地方还未理解
#
# Python练习题：
# 提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递，一定要先写逻辑分析，再写代码。
#
# 1、打印小猫爱吃鱼，小猫要喝水
class Cat(object):
    """
    方法：
    1、喝水
    """

    def __str__(self):
        return "小猫爱吃鱼"

    def catHeShui(self):
        print("小猫要喝水")


xiaomao = Cat()
print(xiaomao)
xiaomao.catHeShui()


# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
class Ren(object):
    """
    属性
    1、名字
    2、体重
    方法
    1、会跑步
    2、吃东西
    """

    def __init__(self, mingzi, tizhong):
        self.mingzi = mingzi
        self.tizhong = tizhong

    def paoBu(self):
        if self.tizhong > 0:
            self.tizhong -= 0.5
            print(f"我跑步了，我重{self.tizhong}")
        else:
            print(f"我没了，你看不到我了")

    def chi(self):
        if self.tizhong < 250:
            self.tizhong += 1
            print(f"我吃了，我重{self.tizhong}")
        else:
            print(f"吃死了")

xiaoming = Ren("xiaoming",75)
xiaomei = Ren("xiaomei",45)
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
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
        return f'户型：{self.mingcheng},总面积：{self.mianji},剩余面积：{self.shengyumianji},内置家具：{self.jiajuliebiao}'


class JiaJu(object):
    def __init__(self, mingcheng, mianji):
        self.mingcheng = mingcheng
        self.mianji = mianji


fangzi1 = FangZi("99层海景房", 15)
chuang = JiaJu("破床", 4)
yigui = JiaJu("破衣柜", 2)
canzhuo = JiaJu("破餐桌", 1.5)
fangzi1.FangJiaJu(chuang)
fangzi1.FangJiaJu(yigui)
fangzi1.FangJiaJu(canzhuo)
print(fangzi1)


# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
class Qiang(object):
    """
    实例属性：
    1、型号
    2、子弹数量
    3、剩余子弹数量

    实例方法：
    1、发射子弹
    2、填装子弹
    """

    def __init__(self, xinghao, zidanshuliang):
        self.xinghao = xinghao
        self.zidanshuliang = zidanshuliang
        self.shegnyuzidan = 0

    def __str__(self):
        return f"{self.xinghao}:可容纳{self.zidanshuliang}发子弹,剩余{self.shegnyuzidan}发子弹"

    def FaSheZiDan(self):
        if self.shegnyuzidan > 0:
            self.shegnyuzidan -= 1
            print(f"{self.xinghao}发射了一发子弹，剩余{self.shegnyuzidan}发子弹")
        else:
            print(f"没子弹了，傻X")

    def TianZhuangZiDan(self):
        if self.shegnyuzidan < self.zidanshuliang:
            self.shegnyuzidan = self.zidanshuliang
            print(f"{self.xinghao}子弹装满了，剩余{self.shegnyuzidan}发子弹")
        else:
            print(f"装不下了，傻X")


class ShiBing(object):
    """
    实例属性：
    1、名字
    2、有枪

    实例方法：
    1、扣动扳机
    2、装子弹
    """

    def __init__(self, mingzi, qiang):
        self.mingzi = mingzi
        self.qiang = qiang

    def __str__(self):
        return f"我叫{self.mingzi}，我有一只{self.qiang}的枪"

    def KouDongBanJi(self):
        self.qiang.FaSheZiDan()

    def ZhuangZiDan(self):
        self.qiang.TianZhuangZiDan()

    def Chakanqiang(self):
        print(f"我看了看{self.qiang}")


ak47 = Qiang("ak47", 30)
ruien = ShiBing("ruien", ak47)

print(ruien)
ruien.KouDongBanJi()
ruien.ZhuangZiDan()
ruien.ZhuangZiDan()
ruien.KouDongBanJi()
ruien.Chakanqiang()
# 5.github新建一个仓库，练习克隆，提交，创建分支，切换分支等
