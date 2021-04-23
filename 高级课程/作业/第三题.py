'''
摆放家具-需求：
1）房子有户型，总面积和家具名称列表
     新房子没有任何家具
2）家具有名字和占地面积，其中床：占4平米 衣柜：占2平米  餐桌：占1.5平米
3）将以上三件家具添加到房子中
4）打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表
'''

class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '[%s] 占地 %.2f' % (self.name, self.area)

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return '户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s' % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        print('要添加 %s' % item)
        if item.area > self.free_area:
            print('%s 的面积太大了，无法添加' % item.name)
            return
            self.item_list.append(item.name)
            self.free_area -= item.area


bed = HouseItem('bed', 400)
print(bed)
chest = HouseItem('chest', 2)
print(chest)
table = HouseItem('table', 1.5)
print(table)


my_home = House('两室一厅', 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)