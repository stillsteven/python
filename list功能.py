from typing import List

list = []

while True:
    a = input("請輸入你要進行的操作：(insert、new、remove、clear)")

    while True:
        if (a == "insert"):
            b = str(input("請輸入你要新增到串列的值："))
            c = int(input("請輸入你要插入到list的地方："))
            list.insert(c, b)
            break
        elif (a == "new"):
            d = str(input("請輸入你要新增的值："))
            list.append(d)
            break
        elif (a == "remove"):
            e = str(input("請輸入你要刪除的數字："))
            list.remove(e)
            break
        elif (a == "clear"):
            list.clear()
            f = str(input("已經刪除字串中所有的數字"))
            break

    print(list)

    g = input("是否繼續輸入(true or false)")
    if (g == "true"):
        continue
    else:
        break
