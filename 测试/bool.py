A = []
A_T = []
AA = []
A3 = []
print("输入一个4阶矩阵，其中每个元素用空格分开，回车键换行") #输入四阶矩阵并列表化
for t in range(4):
    x = list(map(float,input("").split()))
    A.append(x)

A_T = [[A[i][j] for i in range(4)] for j in range(4)]
#通过两个循环对A元素的下角标索引添加到列表A_T中从而转置A
#测试print(A_T)
print("该矩阵的转置矩阵为")
for t in A_T:
    print(t)

AA = [[0] * 4,[0] * 4,[0] * 4,[0] * 4] #定义一个所有元素都是0的四阶矩阵
for i in range(4):         #行和列
    for j in range(4):     #行和列
        for r in range(4): #AA中每个元素需要加4遍
            AA[i][j] = (A[i][r]*A[r][j])+AA[i][j]
print("该矩阵的平方为")
for t in AA:
    print(t)

A3 = [[A[i][j] * 3 for j in range(4)] for i in range(4)]
#循环下角标检索对A中每个元素乘以3并赋给新列表A3
print("三倍该矩阵为")
for t in A3:
    print(t)

