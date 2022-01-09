Sc = []

numberA = input("請輸入A的學號：")
sc1, sc2, sc3 = eval(input("請輸入A的3個考試成績："))
sc = [numberA, sc1, sc2, sc3, sc1+sc2+sc3]
sc = list(map(int, sc))
Sc.append(sc)


numberB = input("請輸入B的學號：")
sc1, sc2, sc3 = eval(input("請輸入B的3個考試成績："))
sc = [numberB, sc1, sc2, sc3, sc1+sc2+sc3]
sc = list(map(int, sc))
Sc.append(sc)


numberC = input("請輸入C的學號：")
sc1, sc2, sc3 = eval(input("請輸入C的3個考試成績："))
sc = [numberC, sc1, sc2, sc3, sc1+sc2+sc3]
sc = list(map(int, sc))
Sc.append(sc)

numberC = input("請輸入D的學號：")
sc1, sc2, sc3 = eval(input("請輸入D的3個考試成績："))
sc = [numberC, sc1, sc2, sc3, sc1+sc2+sc3]
sc = list(map(int, sc))
Sc.append(sc)

numberC = input("請輸入E的學號：")
sc1, sc2, sc3 = eval(input("請輸入E的3個考試成績："))
sc = [numberC, sc1, sc2, sc3, sc1+sc2+sc3]
sc = list(map(int, sc))
Sc.append(sc)

print(Sc)
print(sorted(Sc, key=lambda s: s[4], reverse=True))

Sc.sort(key=lambda s: s[4])
print(Sc)
