# '''
# # 功能描述：定义一个老师类，老师有姓名和性别，还有教的课程，可以教学，实现：XX老师，性别是XX，教XXX课
# # 编写人：
# # 编写日期：
# # 实现逻辑：
# # 1、先定义一个老师类
# # 2、对象有姓名、性别、课程
# #
# # '''
# # # 先定义类
# # class Teacher():
# #     def __int__(self,nema,set,course):
# #         self.nema = nema
# #         self.set = set
# #         self.course = course
# #
# #     def print_info(self):
# #         print(f'老师的姓名是{self.nema}，性别是{self.set}，教的课程是{self.course}')
# #
# # # 再定义对象
# # laoshi = Teacher()
# # laoshi.print_info()



'''
功能描述：有一个空的房子，现在需要放入家具，直到放不下为止
实现逻辑：
1、先定义类别（房子类、家具类）
2、赋予属性：
房子类的（房子地址位置、房子占地面积、房子剩余面积、房子内家具现有列表）
家具类的（家具名称、家具占地面积）
3、实例方法：容纳家具
4、显示房子信息（str打印）

'''

# 先定义类别
class house():
    def __init__(self,location,acreage,):
        self.location = location
        self.acreage = acreage
        self.free_acreage = acreage
        self.furniture = []
class furniture():
    def __init__(self,name,acreage):
        self.name = name
        self.acreage = acreage

