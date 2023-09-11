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

