# %%
# join
L = ["I", "am", "a", "student"]
new_L = "▴".join(L)
print(new_L)
new_L2 = " ".join(L)
print(new_L2)

# %%
# split
L = "I am a student"
new_L = L.split(" ")
print(new_L)

# %%
# 猜數字，三位數
# 1A: 數字存在答案，位子也對
# 1B: 數字存在答案，但是位子錯
ANS = "123"
while True:
    S = input("請輸入三位數(End 離開)")
    if S.upper().strip() == "END":
        break
    result = ""
    for i in range(0, 3):
        if S[i] == ANS[i]:
            result += "A"
        elif S[i] in ANS:
            result += "B"
    # 依照result 結果，輸出xxAxxB
    print("結果為:" +
          str(result.count("A")) +
          "A" +
          str(result.count("B")) +
          "B")
    if result.count("A") == 3:
        break
print("謝謝光臨！")

# %%
# 字典 dictionary
# D = {'Book':'書', 'Desk':'桌子'}
# 字典是用大括號將元素包起來
# 'key':'value'  key不重複
D = {"Good": "好", "Student": "學生"}
print(D["Good"])
D2 = {"A001": ["你好", 3.5, True, 32000],
      "A002": ["meow", 93.3, False, 41000]}
print(D2["A001"])
print(D2["A001"][3])

# %%
# 字典專屬的函數
# dict.items() => key,value 一對對
# dict.keys() => 所有key
# dict.values() => 所有value
D = {"Good": "好", "Student": "學生",
     "Bad": "不好", "Teacher": "老師"}
for mykey, myvalue in D.items():
    print("英文是：" + mykey + " ===> 文是:"
          + myvalue)

# %%%
D = {"Good": "好", "Student": "學生",
     "Bad": "不好", "Teacher": "老師"}
for i, key in enumerate(D.keys(), 1):
    print("第" + str(i) + "個 key是：" + key)

# %%
# 字典 ==> 兩個lists
D = {"Good": "好", "Student": "學生",
     "Bad": "不好", "Teacher": "老師"}
Eng = [i for i in D.keys()]
print(Eng)
chi = [i for i in D.values()]
print(chi)

# %%
S = "I am a student. You are learning Python now."
L = S.split(" ")
print(L)
# 以數字為key的字典
Dict = {i: j for i, j in enumerate(L, 10)}
print(Dict)

# %%
# python 資料結構(容器)
# list串列
# set 集合: 元素不可以重複
# tuple：元素內容不可以更改
S = "I am a student. You are learning Python now!"
remove = "!."
M = ""
for s in S:
    if s not in remove:
        M += s
L = M.split(" ")
S = set(L)
print(S)
L = list(S)
print(L)
dict1 = {i: j for i, j in enumerate(L, 1)}
print(dict1)

# %%
L = [10, 20, 30, 40, 20, 20]
T = tuple(L)
S = set(L)
print(T)
print(S)
# T[1] = 30

# %%
L = [10, 20, 30, 40]
T = tuple(L)
S = set(L)
print(max(L), max(S), max(T))
print(min(L), min(S), min(T))
print(sum(L), sum(S), sum(T))
print(len(L), len(S), len(T))


# %%
# 副程式格式 def 副程式名稱(參數,參數):
# 空四格         身體
# 副程式，就像一個佣人，具有獨立的功能或專長
# 一個主程式，就像主人，可以聘許多不同專長的傭人
def add():
    print("這是副程式")
    print(2 + 3)


print("這是主程式開始...")
add()
print("這是主程式結束...")


# %%
def add(x, y):
    print("這是副程式")
    print(x + y)


print("這是主程式開始...")
a = int(input("第一數："))
b = int(input("第二數："))
add(a, b)
print("這是主程式結束...")


# %%
def add(x, y):
    return x + y


a = 3
b = 5
result = add(a, b)
print(result)

#%%
def add(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

while True:
    choice = input("1.加法 2.減法 3.乘法 4.除法 (輸入End結束)")
    if choice.upper().strip() == "END":
        print("程式終斷")
        break
    a = int(input("第一數："))
    b = int(input("第二數："))
    result = 0
    int_choice = int(choice)
    if int_choice == 1:
        result = add(a,b)
    elif int_choice == 2:
        result = minus(a,b)
    elif int_choice == 3:
        result = multiply(a,b)
    else:
        result = divide(a,b)
    print("您選擇的是：{}，計算結果為：{}".format(choice,result))
