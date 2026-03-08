# 作者:zmz
# 2026年03月08日20时56分32秒
# 1161538248@qq.com
def check(original):
    id1 = input("请输入需要查询的名字:")
    for k in  original:
        if k == id1:
            print(f"{k}的QQ号为{}")
            break
        else:
            print("无这个人的数据")
            break


if __name__ == '__main__':
    dict2 = {"校长": 1,"小王妃":2}
    check(dict2)
