# 作者:zmz
# 2026年03月08日20时53分04秒
# 1161538248@qq.com
import moduel_new, moduel_find, moduel_write

document = {}
try:
    while True:
        print('''欢迎使用【名片管理系统】V2.0
        1. 新建名片
        2. 显示全部
        3. 查询名片
        4. 写入文件
        0. 退出系统''')
        print('-' * 50)
        choice = int(input("请输入一个选择:"))  # input返回字符串类型
        if choice == 1:
            moduel_new.creat(document)
            continue
        if choice == 2:
            print(document)
            continue
        if choice == 3:
            moduel_find.check(document)
            continue
        if choice == 4:
            moduel_write.write(document)
            continue
        if choice == 0:
            break
except ValueError:
    print("输入错误，只能接受到字符串或者数字类型")
