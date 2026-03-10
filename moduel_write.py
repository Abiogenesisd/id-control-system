# 作者:zmz
# 2026年03月20日21时13分14秒
# 1161538248@qq.com
def write(original):
    n = 0
    file = open("list.txt", encoding="utf8", mode="w+")
    for i in original.items():
        n += 1
        file.write(f"{n}号的信息为：{i}\n")
    file.close()


if __name__ == '__main__':
    dict2 = {"1": 2, "2": 2}
    write(dict2)
