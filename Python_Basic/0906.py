#%%
# for loop practice
for i in range(0, 5):
    print(i)
for i in range(0, 10):
    print('A')

#%%
# 計算S從1加到10的總和
# s = 0
# for i in range(1, 11):
#     s = s + i
# print(s)

#%%
# 使用者輸入
# s = 0
# a = int(input("請輸入一數:"))
# for i in range(1, a + 1):
#     s = s + i
# print("1+2+...+", a, "=", s)

#%%
# 起始、終點皆使用者輸入
# start_index = int(input("請輸入起始："))
# end_index = int(input("請輸入終點："))
# total = 0
# for i in range(start_index,end_index+1):
#     total += i
# print(f"從{start_index}加到{end_index}的總和是{total}")

#%%
# 累乘 p = 1 * 2 * 3 * ... * 5
p = 1
end_index = int(input("終點值："))
for i in range(1,end_index+1):
    p *= i
print(f"p從1累乘到{end_index}的結果是{p}")

#%%
"""
印星星1
*
▴*
▴▴*
▴▴▴*
▴▴▴▴*
"""
star_amount = int(input("星星列數："))
for i in range(1,star_amount+1):
    print(f"{(i-1)*' '}*")

#%%
"""
印星星2
    *
   ***
  *****
 *******
"""
star_amount = int(input("星星列數："))
for i in range(1,star_amount+1):
    out = (5-i)*' ' + (2*i - 1) * '*'
    print(out)

#%%
"""
挑戰:
印星星3
*********
 *******
  *****
   ***
    *

"""
star_amount = int(input("星星列數："))
for i in range(1,star_amount+1):
    out = (i-1)*' ' + ((2*star_amount-1)-(2*(i-1))) * '*'
    print(out)

#%%
"""
挑戰:
印數字1
    1
   222
  33333
 4444444
555555555
"""
num_amount = int(input("數字列數："))
for i in range(1,num_amount+1):
    out = (num_amount - i)*' ' + str(i) * (2*i - 1)
    print(out)

#%%
# chr (ascii數值)
# ord (鍵盤的字元)
print(chr(65))
print(chr(66))
for i in range(65,91):
    print(chr(i),end="")

#%%
# 印英文字階層
"""
A
AB
ABC
.
.
ABC...Z
"""
s = ''
for i in range(65,91):
    s += chr(i)
    print(s)

#%%
# 印英文字階層
"""
    A
   BAB
  CBABC
 DCBABCD
    .
    .
    .
Z...A....Z
"""
