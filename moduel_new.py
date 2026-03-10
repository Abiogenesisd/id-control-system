# 作者:zmz
# 2026年03月08日20时56分19秒
# 1161538248@qq.com
def creat(original):
    name = input("请输入名字:")
    qq = input("请输入QQ号码:")
    code = input("请输入电话号码:")
    mail = input("请输入邮件地址:")
    info = {"QQ": qq, "电话号码": code, "邮箱地址": mail}
    original[name] = info


if __name__ == '__main__':
    dict1 = {}
    creat(dict1)
    print(dict1)
