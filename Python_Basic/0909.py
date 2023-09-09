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

# %%
# zip 函數：壓縮、配對
Names = ["張三", "李四", "阿貓"]
Pays = [40000, 42000, 38000]
data_list = list(zip(Names, Pays))
print(data_list)
for name, pay in data_list:
    print("名字：{}\t薪資：{}".format(name, pay))

# %%
Names = ["張三", "李四", "阿貓", "阿狗"]
Pays = [40000, 42000, 38000, 52000]
Sex = [True, False, True, False]
Height = [170, 165, 180, 162]
Title = []
for sex in Sex:
    if sex:
        Title.append("先生")
    else:
        Title.append("女士")
print(Title)
for name, pay, title, height in zip(Names, Pays, Title, Height):
    print(name + title + '您好,您的資料如下：')
    print("薪資：", pay)
    print("身高：", height)

# %%
# L = [10, 20, 40, 30, 60, 45]
# (1) 求加總, 但不用sum(L)直接算, 用for loop算
# (2) 求平均
# (3) 求Max, 但不用max(L), 可參考以下極值範例執行
# (4) 求Min, 但不用min(L), 可參考以下極值範例執行
L = [10, 20, 40, 30, 60, 45]
total_l = 0
for num in L:
    total_l += num
print('加總結果：{}'.format(total_l))

avg_l = total_l / len(L)
print('平均結果：{}'.format(avg_l))

maxNum = -1
for num in L:
    if num > maxNum:
        maxNum = num
print("最大值結果：{}".format(maxNum))

minNum = 1000
for num in L:
    if num < minNum:
        minNum = num
print("最小值結果：{}".format(minNum))

# %%
# Persons = [["張三", 40000, 23],
# 			     ["李四", 42000, 25],
# 			     ["王五", 39000, 30],
# 			     ["陳六", 52000, 42]]
# 寫一個公式
# (1) Pays = [40000, 42000, ...]
# (2) Ages = [23, 25, ...]
# (3) 求出最高薪資,平均薪資,最低薪資
# (4) 列出薪資超過45000的員工
Persons = [["張三", 40000, 23],
           ["李四", 42000, 25],
           ["王五", 39000, 30],
           ["陳六", 52000, 42]]

max_salary = -1
avg_salary = 0
min_salary = 1000000
high_pay_person = []
for name, salary, age in Persons:
    avg_salary += salary
    if salary > max_salary:
        max_salary = salary
    if salary < min_salary:
        min_salary = salary
    if salary > 45000:
        high_pay_person.append([name, salary, age])

avg_salary /= len(Persons)
print("最高薪資:{}\n平均薪資:{}\n最低薪資:{}\n列出薪資超過45000的員工:{}"
      .format(max_salary, int(avg_salary), min_salary, high_pay_person))

# %%
