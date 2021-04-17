# try:
#     f = open('test.txt','r')
# except:
#     f = open('test.txt','w')
#
#
# try:
#     print(num)
# except (IndexError,ImportError,NameError) as result:
#     print(result)

# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:
#     print('我是else,是没有异常的时候执行的代码')
# finally:
#     print('有没有异常，我都会执行')


import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
 # 如果在读取⽂件的过程中，产⽣了异常，那么就会捕获到
 # ⽐如 按下了 ctrl+c
        print('意外终⽌了读取数据')
    finally:
        f.close()
        print('关闭⽂件')
except:
 print("没有这个⽂件")