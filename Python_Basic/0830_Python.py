print(2+3,2*3)
print("3*5=",3*5)
print("姓名：","張三")

print('你好，%s，今天是星期%s，晚上%d點,%.2f'%('chris','三',8,3.3333))
a = "嗨！" + "你好"
print(a)
#  can only concatenate str (not "int") to str
# b = "嗨！" + (3*3)
# print(b)
# 複製
c = "張三" * 20
print(c)
age = 32
if age >= 20:
    print('可以買菸')
else:
    print('不行')