# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。


index = int(input("你需要第几项"))

num1 = 0
num2 = 1
count = 2

if index <= 0:
    print("请输入一个正整数")
elif index == 1:
    print("斐波那契数列：")
    print(num1)
else:
    print("斐波那契数列：")
    print(num1, ",", num2, end=" , ")
    while count < index:
        nth = num1 + num2
        print(nth, end=" , ")
        # 更新值
        num1 = num2
        num2 = nth
        count += 1
