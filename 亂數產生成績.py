import random

x, y = eval(input("請輸入你要測試幾位學生的幾項成績?兩數字請用逗號分開"))
z = []
for a in range(1, x+1):
    z.append([])

for i in range(1, x+1):
    z[i-1].append(i)
    for j in range(1, y+1):
        k = random.randint(1, 99)
        z[i-1].append(k)
    z[i-1].append(sum(z[i-1][1:y+1]))
    z[i-1].reverse()

b = sorted(z, reverse=True)

for c in range(1, x+1):
    z[c-1].reverse()

print("原始產生的串列如下:\n", z)
print("排序過的成績如下\n", b)
