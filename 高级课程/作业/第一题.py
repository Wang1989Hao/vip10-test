'''
需求：打印小猫爱吃鱼，小猫要喝水
分析：
1、先有类，再有对象
2、类：爱吃鱼、要喝水
3、对象：小猫
4、采用不带参数的_init_()魔法方法
'''
# 定义类
class Cat():
    # 定义初始化功能的函数
    def __init__(self):
        # 添加实例属性
        self.fish = '吃'
        self.water = '喝'

    def print_info(self):
        # 类里面调用实例属性
        print(f'kitteny爱{self.fish}鱼')
        print(f'kitteny要{self.water}水')

kitteny = Cat()
kitteny.print_info()