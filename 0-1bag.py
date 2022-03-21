import numpy as np
import time
import matplotlib.pyplot as plt


print("请选择使用方法：1.贪心法 2.动态规划法 3.回溯法")
n=int(input())
if n==1:
    def Initial():
        print("输入背包容量:")
        weight_most = int(input())
        weight = list(map(int, input("输入重量,空格分开:").split()))
        value = list(map(int, input("输入价值,空格分开:").split()))
        item = list(zip(weight, value))
        #print("重量，价值：" + item.__str__() + "\n背包容量：" + weight_most.__str__())
        return item, weight_most,weight,value

    def main():
        start = time.time()
        item0, weight_most,weight,value = Initial()
        item = np.array(item0)
        idex_weight = Weight(item)
        idex_price = Price(item)
        idex_Density = Density(item)
        number = len(item)
        data = np.array(item)
        data_list = [0] * number
        for i in range(number):
            data_list[i] = (data[i, 1]) / (data[i, 0])
        data_set = np.array(data_list)
        print("非递增排序:",data_set)
        results_weight = GreedyAlgo(item, weight_most, idex_weight)
        results_Price = GreedyAlgo(item, weight_most, idex_price)
        results_Density = GreedyAlgo(item, weight_most, idex_Density)
        results = Compare(results_weight, results_Price, results_Density)
        print("贪心法最优解：",results[1])
        print("是否打印散点图？")
        m = input()
        if m == 'y' or 'Y':
            plt.figure(figsize=(10, 10), dpi=100)
            plt.scatter(weight,value)
            plt.show()
        elif m == 'n' or 'N':
            pass
        end = time.time()
        s = end - start
        print("运行时间：", s)
        with open('test.txt','a') as file0:
            print('%s' % '贪心法最优解：','%d' % results[1],'%s' % '求解时间：','%d' % s,file=file0)



    def Weight(item):
        data = np.array(item)
        idex = np.lexsort([-1 * data[:, 1], data[:, 0]])
        return idex


    def Price(item):
        data = np.array(item)
        idex = np.lexsort([data[:, 0], -1 * data[:, 1]])
        return idex


    def Density(item):
        number = len(item)
        data = np.array(item)
        data_list = [0] * number
        for i in range(number):
            data_list[i] = (data[i, 1]) / (data[i, 0])
        data_set = np.array(data_list)
        idex = np.argsort(-1 * data_set)
        return idex


    def GreedyAlgo(item, weight_most, idex):
        number = len(item)
        status = [0] * number
        total_weight = 0
        total_value = 0
        for i in range(number):
            if item[idex[i], 0] <= weight_most:
                total_weight += item[idex[i], 0]
                total_value += item[idex[i], 1]
                status[idex[i]] = 1
                weight_most -= item[idex[i], 0]
            else:
                continue
        return total_weight, total_value, status


    def Compare(total_value1, total_value2, total_value3):
        values = zip(total_value1, total_value2, total_value3)
        data = np.array([total_value1[1], total_value2[1], total_value3[1]])
        idex = np.argsort(data)
        value = list(zip(*values))
        results = list(value[idex[2]])
        return results
    main()



if n==2:
    start = time.time()
    print("输入背包容量:")
    weight_most = int(input())
    weight = list(map(int, input("输入重量,空格分开:").split()))
    value = list(map(int, input("输入价值,空格分开:").split()))
    item = list(zip(weight, value))
    number = len(item)
    data = np.array(item)
    data_list = [0] * number
    for i in range(number):
        data_list[i] = (data[i, 1]) / (data[i, 0])
    data_set = np.array(data_list)
    print("非递增排序:", data_set)
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
    end=time.time()
    print("动态规划法最优解：",result)
    print("是否打印散点图？")
    m = input()
    if m=='y' or 'Y':
        plt.figure(figsize=(10, 10), dpi=100)
        plt.scatter(weight[1:],value[1:])
        plt.show()
    if m=='n' or 'N':
        pass
    s=end-start
    print("运行时间：",s)
    with open('test.txt', 'a') as file0:
        print('%s' % '动态规划法最优解：', '%d' % result, '%s' % '求解时间：', '%d' % s, file=file0)


if n==3:
    bestV = 0
    curW = 0
    curV = 0
    bestx = None
    start=time.time()
    print("输入背包容量:")
    weight_most = int(input())
    weight = list(map(int, input("输入重量,空格分开:").split()))
    value = list(map(int, input("输入价值,空格分开:").split()))
    item = list(zip(weight, value))
    number = len(item)
    data = np.array(item)
    data_list = [0] * number
    for i in range(number):
        data_list[i] = (data[i, 1]) / (data[i, 0])
    data_set = np.array(data_list)
    print("非递增排序:", data_set)

    def backtrack(i):
        global bestV, curW, curV, x, bestx
        if i >= n:
            if bestV < curV:
                bestV = curV
                bestx = x[:]
        else:
            if curW + weight[i] <= weight_most:
                x[i] = True
                curW += weight[i]
                curV += value[i]
                backtrack(i + 1)
                curW -= weight[i]
                curV -= value[i]
            x[i] = False
            backtrack(i + 1)
    x=[False for i in range(n)]
    backtrack(0)
    print("回溯法最优解：",bestV)
    end=time.time()
    print("是否打印散点图？")
    m = input()
    if m == 'y' or 'Y':
        plt.figure(figsize=(10, 10), dpi=100)
        plt.scatter(weight, value)
        plt.show()
    elif m == 'n' or 'N':
        pass
    s=end-start
    print("运行时间：",s)
    with open('test.txt', 'a') as file0:
        print('%s' % '回溯法最优解：', '%d' % bestV, '%s' % '求解时间：', '%d' % s, file=file0)
    #print(bestx)
