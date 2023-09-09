# %%
# input
name = input("請輸入姓名:")
print(name)

# %%
A = '123'
B = int(A)
print(type(A))
print(type(B))
# can only concatenate str (not "int") to str
# print(A+1)
print(B + 3)

# %%
# 資料型態轉換
# int(字串)==>整數值
# str(數值)==>字串
# bool(整數1) ==> True, bool(整數0)==>False
# int(bool) ==>整數, int(True)=1, int(False)=0
name = input('姓名：')
age = str(input('年紀：'))
print(type(age))

# %%
# 變數 = int(input(“提示字串”))
age = int(input("age is:"))
print(age, type(age))

# %%
# 輸入稅率0.06, 輸入底薪40000
# 計算所得稅及實薪，並輸出
tax_rate = float(input('輸入稅率:'))
salary = int(input('輸入底薪:'))
income_tax = int(salary * tax_rate)
real_salary = int(salary * (1 - tax_rate))
print(f"所得稅:{income_tax} 及 實薪:{real_salary}")

# %%
# if else
Age = int(input("年紀："))
if Age > 20:
    print('too old')
else:
    print('too young')

# %%
Age = int(input("年紀："))
if Age < 40:
    if Age < 20:
        print('未成年')
    else:
        print('成年人')
else:
    if Age < 65:
        print('中年人')
    else:
        print('老年人')
print('謝謝光臨')

# %%
# 使用elif
Age = int(input("年紀："))
# 自左而右
if Age < 20:
    print('年輕人')
elif Age < 40:
    print('成年人')
elif Age < 65:
    print('中年人')
else:
    print('老年人')
print('謝謝光臨')

# %%
# 自右而左
Age = int(input("年紀："))
if Age > 65:
    print('老年人')
elif Age > 40:
    print('成年人')
elif Age > 20:
    print('中年人')
else:
    print('年輕人')
print('謝謝光臨')
