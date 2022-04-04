import tkinter as tk
import numpy as np
import time
import matplotlib.pyplot as plt

window = tk.Tk()
window.title('{0-1}KP 实例数据集算法实验平台')
window.geometry('500x500')
#定义一个lable
l = tk.Label(window,text='请选择方法并输入数据',font=('Arial',12))
l.pack() #固定窗口位置

l1 = tk.Label(window,text='输入背包容量',font=('Arial',12))
l1.pack()
e1=tk.Entry(window,show=None)
e1.pack()
l2 = tk.Label(window,text='输入重量',font=('Arial',12))
l2.pack()
e2=tk.Entry(window,show=None)
e2.pack()
l3 = tk.Label(window,text='输入价值',font=('Arial',12))
l3.pack()
e3=tk.Entry(window,show=None)
e3.pack()

def insert_point3():
    var1 = e1.get()
    var2 = e2.get()
    var3 = e3.get()
    start = time.time()
    weight_most = int(var1)
    weight = list(map(int, var2.split()))
    value = list(map(int, var3.split()))
    item = list(zip(weight, value))
    number = len(item)
    data = np.array(item)
    data_list = [0] * number
    for i in range(number):
        data_list[i] = (data[i, 1]) / (data[i, 0])
    data_set = np.array(data_list)
    print("非递增排序:", data_set)
    print(weight_most,weight,value)

    def Dynamic(weight, value, weight_most):  # return max value
        num = len(weight)
        weight.insert(0, 0)  # 前0件要用
        value.insert(0, 0)  # 前0件要用
        bag = np.zeros((num + 1, weight_most + 1), dtype=np.int32)  # 下标从零开始
        for i in range(1, num + 1):
            for j in range(1, weight_most + 1):
                if weight[i] <= j:
                    bag[i][j] = max(bag[i - 1][j - weight[i]] + value[i], bag[i - 1][j])
                else:
                    bag[i][j] = bag[i - 1][j]
        # print(bag)
        return bag[-1, -1]

    result = Dynamic(weight, value, weight_most)
    end = time.time()
    #print("动态规划法最优解：", result)
    #plt.figure(figsize=(10, 10), dpi=100)
    #plt.scatter(weight[1:], value[1:])
    #plt.show()
    s = end - start
    #print("运行时间：", s)
    txt.insert(result)


b1 = tk.Button(window,text="用贪心法求解",width=15,height=2,command=None)
b1.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)
b2 = tk.Button(window,text="用回溯法求解",width=15,height=2,command=None)
b2.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
b3 = tk.Button(window,text="用动态规划法求解",width=15,height=2,command=insert_point3)
b3.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)
l3 = tk.Label(window,text='结果如下',font=('Arial',12))
l3.place(x=220,y=250)
txt= tk.Text(window)
txt.place(x=110,y=280)


window.mainloop()
