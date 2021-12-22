import math


def factor(num):
    factors = []
    for_times = int(math.sqrt(num))
    for i in range(for_times + 1)[1:]:
        if num % i == 0:
            factors.append(i)
            t = int(num / i)
            if not t == i:
                factors.append(t)
    return factors


a = int(input("請輸入你要找出因數及最大公因數的第一個數字? "))
b = int(input("請輸入你要找出因數及最大公因數的第二個數字? "))
print(a, "的因數有", factor(a))
print(b, "的因數有", factor(b))
print("兩數的最大公因數是", math.gcd(a, b))
