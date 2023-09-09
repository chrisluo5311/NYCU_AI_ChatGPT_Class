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
