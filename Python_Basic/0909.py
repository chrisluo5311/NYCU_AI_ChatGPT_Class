# %%
# 串列好用的函數
# len(list): 傳回串列的長度，即元素的個數
# max(list): 傳回最大的元素
# min(list): 傳回最小的元素
# sum(list): 傳回元素的總和
L = [10, 30, 20, 40]
print(len(L))
for i in range(0, len(L)):
    print(L[i], end=',')

# %%
L = [10, 30, 20, 40, 50, 60]
print("最大數為：", max(L))
print("min:", min(L))
print("sum:", sum(L))
print("average:", sum(L) / len(L))

# %%
L = [["張三", 23, 170, 40000],
     ["李四", 30, 165, 42000],
     ["王五", 42, 180, 52000],
     ["陳六", 52, 155, 53000]]
print("大家的薪資陳列如下：", end=" ")
for i in range(0, len(L)):
    # print(L[i])
    print(L[i][3], end=',')

# %%
# 串列的元素的增刪改
# 改 list[位置]=新質
L1 = [10, 20, 30, 40]
L1[1] = 25
print(L1)
# 刪除元素 del list[位置]
# 刪除list del list
del L1[2]
print(L1)
# 新增 list.append(新元素)
L1.append(80)
print(L1)
M = ["張三", "李四", "阿貓", "阿狗"]
Sex = [True, False, True, False]
N = []
for i in range(0, len(M)):
    if Sex[i]:
        N.append(M[i])
print(N)

# %%
M = ["張三", "李四", "阿貓", "阿狗"]
print(M[0:2])
print(M[0:4:3])

# %%
# 串列遍歷

L = [10, 20, 30, 40]
for x in L:
    print(x)
Names = ["張三", "李四", "阿貓", "阿狗"]
# 這種寫法失去位置控制權將產生負面後果
for name in Names:
    print(name, end=' ')

# %%
# enumerate 會多給一個索引
Names = ["張三", "李四", "阿貓"]
Pays = [40000, 42000, 38000]
for i, name in enumerate(Names):
    print("索引：{}\t名字:{}\t薪資:{}".format(i, name, Pays[i]))
    if Pays[i] >= 40000:
        print('薪水大於四萬的有：{}'.format(name))
    else:
        print('薪水好低的人是：{}'.format(name))
# 指定索引
L = [10, 20, 30, 40]
for i, num in enumerate(L, start=1):
    print('索引:{}\t數值:{}'.format(i, num))

# %%
# 印出張三女士 李四先生
Names = ["張三", "李四", "阿貓", "阿狗"]
Sex = [True, False, True, False]
for i, name in enumerate(Names):
    if Sex[i]:
        print('{}女士'.format(name))
    else:
        print('{}先生'.format(name))

# %%
Names = ["張三", "李四", "阿貓", "阿狗"]
Sex = [True, False, True, False]
Title = ['女士', '先生']
# int(True)==>1, int(False)==>0
for i, name in enumerate(Names):
    out = name + Title[int(Sex[i])]
    print(out)
