# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

print("10000以内的阿姆斯特朗数有：")
for number in range(1, 10001):
    if  number < 10: #1-9都为阿姆斯特朗数，直接输出即可
        print(number)
    elif number < 100:
        n1 = number % 10 #取个位数
        n2 = int(number/10 % 10) #取十位数
        result = n1**2 + n2**2
        if number == result:
            print(number)
    elif number < 1000:
        n1 = number % 10
        n2 = int(number/10 % 10)
        n3 = int(number/100 % 10) #取千位数
        result = n1**3 + n2**3 + n3**3
        if number == result:
            print(number)
    elif number < 10000:
        n1 = number % 10
        n2 = int(number/10 % 10)
        n3 = int(number/100 % 10)
        n4 = int(number/1000 % 10) #取万位数
        result = n1**4 + n2**4 + n3**4 + n4**4 #各位数进行次方运算
        if number == result:
            print(number)
