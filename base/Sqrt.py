import cmath

Num = int(input("请输入一个数字："))

NumSqrt = cmath.sqrt(Num)

print('{0} 的平方根为 {1:0.3f}'.format(Num ,NumSqrt.real))
