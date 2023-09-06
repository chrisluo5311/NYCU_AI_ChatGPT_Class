print(2+3,2*3)
print("3*5=",3*5)
print("姓名：","張三")

#%%
print('你好，%s，今天是星期%s，晚上%d點,%.2f'%('chris','三',8,3.3333))
a = "嗨！" + "你好"
print(a)

#%%
# can only concatenate str (not "int") to str
# b = "嗨！" + (3*3)
print(b)

#%%
# 複製
c = "張三" * 20
print(c)
age = 32
if age >= 20:
    print('可以買菸')
else:
    print('不行')

#%%
#  bool
print(1 > 2)
print(3 == 3)

#%%
# type 資料型態
print(type(23.4))
print(type('hi'))
print(type(3))
print(type(True))

#%%
chi = 90
eng = 60
total = chi + eng
avg = total / 2
print("總分：", total,"分")
print("平均：", int(avg),"分")

#%%
salary = 40000
tax_rate = 0.06
income_tax = salary * tax_rate
real_salary = salary * (1 - tax_rate)
print(int(income_tax), int(real_salary))