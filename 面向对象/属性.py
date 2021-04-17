# class Washer():
#     def wash(self):
#         print('我会洗衣服')
#
# hair1 = Washer()
#
# hair1.width = 500
# hair1.heigeht = 800
#
# print(f'hair1洗衣机的高度是{hair1.width}')
# print(f'hair1洗衣机的宽度是{hair1.heigeht}')

class Washer():
    def __init__(self,width,height,brand):
        self.width = width
        self.height = height
        self.brand = brand

    def print_info(self):
        print(f'洗衣机的宽度是{self.width},高度是{self.height}，品牌是{self.brand}')

    def __str__(self):
        return f'这是{self.brand}洗衣机的品牌说明书'

    def __del__(self):
        print(f'{self}对象已经被删除')

haier1 = Washer(10,20,'海尔')
print(haier1)
haier1.print_info()

haier2 = Washer(30,40,'西门子')
print(haier2)
haier2.print_info()