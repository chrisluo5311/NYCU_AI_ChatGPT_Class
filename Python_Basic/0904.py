# %%
# 變數
x, y = 3, 5
a = b = c = 10
print(x, y)
print(a, b, c)

# %%
x = 5
x += 2
print(x)

# %%
# print 多種變化
# \n: 換行
# \t: tab
# end: print('xx',end="")
# format print("...{}...{}".format(a,b))
# print("姓名:{} 年齡:{}".format("阿貓", 11))
Name = "張三"
Age = 22
Weight = 65.4
print("姓名:%s 年齡:%d 重量:%.1f" % (Name, Age, Weight))

# %%
# print指令結束一定會換行
# 若print() 不想換行，可以用end=""
for i in range(0, 10):
    print(i, end='')

# %%
# and, or
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-----')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('-----')
print(not True)
print(not False)

# %%
Choice = int(input("請輸入選擇(1.新增 2.刪除 3.修改 4.列印 5.離開)"))
if 1 <= Choice <= 5:
    print("輸入正確")
else:
    print("輸入錯誤")

# %%
# for 迴圈
# range(起始值,終止值,跳躍)
p = [i for i in range(0, 10, 2)]
print(p)

for i in range(0, 5):
    print('A', end='')

# %%
for i in range(0, 5):
    print(2 * i + 1)

# %%
s = 0
for i in range(1, 11):
    s += i
print(s)
