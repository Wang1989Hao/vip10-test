'''
士兵开枪-需求：
1）士兵瑞恩有一把AK47
2）士兵可以开火（士兵开火扣动的是扳机）
3）枪 能够 发射子弹（把子弹发射出去）
4）枪 能够 装填子弹-增加子弹的数量
'''

class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print('[%s] 没有子弹了...' % self.model)
            return
        self.bullet_count -= 1
        print('[%s] 突突突...[%d]' %(self.model,self.bullet_count))


class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun == None:
            print('[%s] 还没有枪' %self.name)
            return
        print('go!!! [%s]' %self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun('AK47')
ryan = Soldier('Ryan')
ryan.gun = ak47
ryan.fire()