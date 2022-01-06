from tkinter import *
import random

dict1 = {}
# ========================================功能定義區========================================


def enterdict():  # 定義按鈕功能
    dict1[int(e2.get())] = e3.get()
    e2.delete(0, END)  # 按完確認加入後刪除e2裡的文字
    e3.delete(0, END)  # 按完確認加入後刪除e2裡的文字


def show():  # 測試讀取資料用(寫完請註解掉)
    print(dict1)


def guess():
    r = 0
    k = random.randint(1, 4)

    if r == 0:
        r = 1
    else:
        r = 0

    if r == 1:
        label7 = Label(window, text=(k)
                       ).grid(row=2, column=3)  # 隨機產生數字(1到4)
    else:
        label7 = Label(window, text=(k)
                       ).grid(row=2, column=3)  # 隨機產生數字(1到4)

    if ((k == 1 and int(e4.get()) == 2) or (k == 2 and int(e4.get()) == 3) or (k == 3 and int(e4.get()) == 4) or (k == 4 and int(e4.get()) == 1)):
        label9 = Label(window, text="你輸").grid(row=3, column=3)
    elif ((k == 2 and int(e4.get()) == 1) or (k == 3 and int(e4.get()) == 2) or (k == 4 and int(e4.get()) == 3) or (k == 1 and int(e4.get()) == 4)):
        label9 = Label(window, text="你1贏").grid(row=3, column=3)
    else:
        label9 = Label(window, text="平手").grid(row=3, column=3)

    label8 = Label(window, text=("                                ")).grid(
        row=3, column=1)

    label8 = Label(window, text=("結果", dict1[int(e4.get())], "吃", dict1[k])).grid(
        row=3, column=1)


def playagain():
    e4.delete(0, END)
    label7 = Label(window, text=" "
                   ).grid(row=2, column=3)  # 隨機產生數字(1到4)
    label9 = Label(window, text="      ").grid(row=3, column=3)


# ========================================功能定義、界面分隔線========================================
# 第一界面程式開始

window = Tk()
window.title("GUI遊戲")  # 標題
window.geometry("300x160")  # 視窗大小

# 標籤
label = Label(window, text="Label字典準備", bg="white",
              width=15).grid(row=0, column=1)
label1 = Label(window, text="字典名稱").grid(row=1)
label2 = Label(window, text="對應鍵").grid(row=2)
label3 = Label(window, text="對應值").grid(row=3)

# 輸入框
e1 = Entry(window)  # 字典名稱輸入框
e1.insert(1, "dict1")
e2 = Entry(window)  # 對應鍵輸入框
e3 = Entry(window)  # 對應值輸入框

# 定位輸入框
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

# 按鈕 (每個按鈕需個別定義功能)
btn1 = Button(window, text="確認加入", command=enterdict)
btn2 = Button(window, text="建立完成", command=window.destroy)
btn3 = Button(window, text="test", command=show)  # 測試讀取資料用(寫完請註解掉)

# 定位按鈕
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)  # 測試讀取資料用(寫完請註解掉)


window.mainloop()  # 第一個界面最後一行

# ========================================第一第二界面分隔線========================================

# 以下是按下建立完成後的介面(第二個界面)
window = Tk()
window.title("GUI遊戲")  # 標題
window.geometry("400x160")  # 視窗大小

# 標籤
label4 = Label(window, text="遊戲進行中", bg="white",
               width=15).grid(row=0, column=2)
label5 = Label(window, text="你出").grid(row=1, column=1)
label6 = Label(window, text="電腦出").grid(row=1, column=3)


# 輸入框
e4 = Entry(window)  # 你出什麼的輸入框

# 定位輸入框
e4.grid(row=2, column=1)

# 按鈕 (每個按鈕需個別定義功能)
btn4 = Button(window, text="猜", command=guess)
btn5 = Button(window, text="再玩一次", command=playagain)
btn6 = Button(window, text="結束", command=window.destroy)
btn7 = Button(window, text="test", command=show)  # 測試讀取資料用(寫完請註解掉)

# 定位按鈕
btn4.grid(row=2, column=2)
btn5.grid(row=4, column=1)
btn6.grid(row=4, column=2)
btn7.grid(row=4, column=3)  # 測試讀取資料用(寫完請註解掉)


window.mainloop()  # 第二個界面最後一行(程式結束)

