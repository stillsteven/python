import random

while True:
    k = random.randint(1, 4)
    dict = {1: '棒子', 2: '老虎', 3: '雞', 4: '蟲'}

    a = int(input("請問你出什麼(1是棒子、2是老虎、3是雞、4是蟲)"))

    print("隨機數是 ", k)
    print("你出", dict[a], "電腦出", dict[k])

    if ((k == 1 and a == 2) or (k == 2 and a == 3) or (k == 3 and a == 4) or (k == 4 and a == 1)):
        print("結果...你輸了")
    elif ((k == 2 and a == 1) or (k == 3 and a == 2) or (k == 4 and a == 3) or (k == 1 and a == 4)):
        print("結果...你贏了")
    else:
        print("結果...平手")

    z = input("play again?(yes or not)")
    if z == ("yes"):
        continue
    else:
        break
