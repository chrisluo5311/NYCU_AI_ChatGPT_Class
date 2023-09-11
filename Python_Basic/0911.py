# %%
# list comprehension
# 生成的 list = [生成元素運算式 for 範圍 if 條件]
# (1) 執行一次的for迴圈
# (2) 判斷條件是否為真
# (3) 若條件為真==>生成元素 否則==>不做事(不生成)
# 回到(1)
L1 = [i for i in range(1, 6)]
print(L1)

# 生成元素可以是一個運算式
L2 = [2 * i for i in range(1, 6)]
print(L2)

# 加上條件，滿足條才生成
new_data = [i for i in range(1, 11) if i % 2 == 0]
print(new_data)

# %%
Ages = [22, 45, 33, 69, 42]
# 希望將40歲以下的年紀抓出來形成一個Young的list
Young = [age for age in Ages if age < 40]
print(Young)
Young1 = [str(age) + '歲' for age in Ages if age < 40]
print(Young1)

# %%
Names = ['張三', '李四', '阿貓', '阿狗']
Pays = [42000, 35000, 53000, 48000]
# 高薪姓名放入High list, 低薪姓名放入Low list
High = [name for name, pay in zip(Names, Pays) if pay > 50000]
Low = [name for name, pay in zip(Names, Pays) if pay <= 50000]
print(High)
print(Low)

# %%
Names = ['張三', '李四', '阿貓', '阿狗']
Sex = [True, False, False, True]  # True:男生 False:女生
# 請將男生的姓名，收錄在Mens的list
men_list = [name for (name, sex) in zip(Names, Sex) if sex]
print(men_list)

# 老師版：男生加上先生 女生加上女士
Title = ['女士', '男士']
all_list = [name + Title[int(sex)] for (name, sex) in zip(Names, Sex)]
print(all_list)

# chris版：男生加上先生 女生加上女士
full_list = [name + '男士' if sex else name + '女士' for (name, sex) in zip(Names, Sex)]
print(full_list)

# %%
# L = [ [for j in range(0,3)] for i in range(0,3)]
L = [[int(i == j) for j in range(0, 3)] for i in range(0, 3)]
print(L)

# %%
# nested list comprehension
# 生成二維
L = [[j for j in range(1, 6)] for i in range(1, 6)]
print(L)

# 二維降成一維
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [j for i in matrix for j in i]
print(flattened)

# %%
# 字串和list的緊密關係
# 字串可視為一個list, 每個字母都當作是list中的一個元素
S = 'ABCD'
for i in range(0, 4):
    print(S[i], end='')
print()
for s in S:
    print(s, end='')

# %%
# 元素 in 集合 ==> True 或 False
S = 'ABCD'
print('A' in S)
print(not ('A' in S))
print('A' not in S)
print('X' in S)

# %%
S = 'I am a student. I am learning Python!'
Remove = '.!'
M = ''
for s in S:
    if s not in Remove:
        M += s
print(M)

# %%
# 字串相關的函數
# split()
# 字串.split(分割符號) => 以分割符號拆解字串，並放入list中
S = 'I am a student.'
str_list = S.split(' ')
print(str_list)
back_to_str = '#'.join(str_list)
print(back_to_str)

S2 = 'I am a student. I am learning Python. Good!'
L = S2.split('.')
print(L)

# 先去除句子中不要的符號
# 再把句子分割，將單字放入list中
S3 = 'I am a student. I am learning Python! It is very good.'
# 輸出 V = [單字,單字,...]
remove_str = ".!"
M = ''
for s in S3:
    if s not in remove_str:
        M += s
print(M)
V = M.split(' ')
print(f"V:{V}")

# join()
# 字串 = 合併符號.join(list)
L = ["A", "B", "C", "D"]
# 輸出 "A#B#C#D"
new_str = '#'.join(L)
print(new_str)

# %%
# 字串常用函數
# max() 通用
# 字串.upper() 小寫換大寫
# 字串.lower() 大小換小寫
# 字串.title() 第一個字母換成大寫,其他字母都小寫
# 字串.swapcase() 大寫換小寫 ＆ 小寫換大寫
S = "welCome"
print(S.upper())
print(S.lower())
print(S.swapcase())
print(S.title())

# %%
# 字串去除前後空白
# 字串.strip() 去掉首尾空白
# 字串.lstrip() 去掉左邊空白
# 字串.rstrip() 去掉右邊空白
# 字串.count(字母) 計算某字母出現在字串的次數
S = ' racecar '
print(S.strip())
print(S.lstrip())
print(S.rstrip())
print(S.count("r"))

# %%
A = input("請輸入選項：Ａ.新增 Ｂ.修改 C.查詢 D.列印 End表結束")
input_txt = A.strip().upper()
if input_txt == "END":
    print("謝謝光臨")
else:
    print("輸入為:", A)

# %%
# while 迴圈
# while 條件：
i = 1
while i < 5:
    print(i)
    i += 1

# %%
# while True
# 1. break: 跳離迴圈
# 2. continue: continue後不執行，回到head
while True:
    A = input("輸入(End結束)：")
    if A.strip().upper() == "END":
        print("你已按下結束鍵")
        break
    print('您輸入的是：', A)

