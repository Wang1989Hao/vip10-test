'''
需求：小明爱跑步，爱吃东西。
1）小明体重70.5公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤

分析：可用带参数的__init__()和__str__()魔法方法
姓名、体重是属性，吃饭、跑步是2个方法，而小明和小美就是对象，调用跑步的方法就是减体重，调用吃饭的方法就是增加体重。
'''
class People():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'我的名字叫{self.name},爱跑步，爱吃东西，体重是{self.weight}公斤'

    def run(self):
        print(f'每次跑步会减肥{self.weight}公斤')
        self.weight -= 0.5

    def eat(self):
        print(f'每次吃东西会体重会增加{self.weight}公斤')
        self.weight += 1

    # def print_info(self):
    #     print(f'小明吃跑步，爱吃东西，现在小明的体重是{self.weight}公斤,每次跑步会减肥{self.lose_weight}公斤，每次吃东西体重会增加{self.put_on_weight}公斤')
    #     print(f'小美的体重是{self.weight}公斤')
xiaoming = People('小明',75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = People('小美',45)
# xiaomei.run()
# xiaomei.eat()
print(xiaomei)