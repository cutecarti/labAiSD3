# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х
# равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми
# числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.
# 11. Формируется матрица F следующим образом: если в С сумма чисел  в нечетных столбцах в области 2 больше,
# чем произведение чисел в четных строках в области 1, то поменять в С симметрично области 2 и 3 местами, иначе Е и В
# поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: (К*A)*А– (K * AT).
# Выводятся по мере формирования А, F и все матричные операции последовательно.
import random


def MonK(list,k):
    for i in range(len(list)):
        for j in range(len(list)):
            list[i][j] = int(list[i][j])*k
    return list
def MonM(list1,list2):
    res = [[0 for x in range(len(list1))] for y in range(len(list2))]
    for i in range(len(list1)):
        for j in range(len(list2[0])):
            for k in range(len(list2)):
                res[i][j] += list1[i][k] * list2[k][j]
    return res

def transpose(list):
    res = [[0 for j in range(len(list))]for i in range(len(list))]
    for i in range(len(list)):
        for j in range(len(list)):
            res[j][i] = list[i][j]
    return res
def MminusM(list1,list2):
    res = [[0 for x in range(len(list1))]for x in range(len(list1))]
    for i in range(len(list1)):
        for j in range(len(list1)):
            res[i][j] = list1[i][j] - list2[i][j]
    return res
def printout(list):
    for i in list:
        for j in i:
            print(j,end='\t')
        print('',end='\n')

print('Введите число K:')
k = int(input())
print('Введите число N')
n = int(input())
A = []
crutch = []
s = 0
print('Выберете вариант заполнения(0 - ручное заполнение. 1 - случайное заполнение)')
choise = input()
if choise == '0':
    #до выбора ручного заполнения измените число в коде заполнения nums
    nums = [1 for x in range(n*n)]
else:
    nums = [random.randint(-10,10) for x in range(n*n)]
for i in nums:
    crutch.append(i)
    if len(crutch) == n:
        A.append(crutch)
        crutch = []
crutch = []
E,B,D,C = [],[],[],[]
print('Построенная матрица А:')
printout(A)
if n % 2 == 0:
    for i in range (n):
        for j in range (n):
            if (j <= n/2-1)and(i <= n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    E.append(crutch)
                    crutch = []
            if (j > n/2-1)and(i <= n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    B.append(crutch)
                    crutch = []
            if (j <= n/2-1)and(i > n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    D.append(crutch)
                    crutch = []
            if (j > n/2-1)and(i > n/2-1):
                crutch.append(A[i][j])
                if len(crutch) == n/2:
                    C.append(crutch)
                    crutch = []
else:
    for i in range (n):
        for j in range (n):
            if (j<=n//2-1) and (j != n//2) and (i <=n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    E.append(crutch)
                    crutch = []
            if (j>n//2-1) and (j != n//2) and (i <=n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    B.append(crutch)
                    crutch = []
            if (j<=n//2-1) and (j != n//2) and (i > n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    D.append(crutch)
                    crutch = []
            if (j>n//2-1) and (j != n//2) and (i > n//2-1) and (i != n//2):
                crutch.append(A[i][j])
                if len(crutch) == n//2:
                    C.append(crutch)
                    crutch = []
print('Построенная матрица E:')
printout(E)
print('Построенная матрица B:')
printout(B)
print('Построенная матрица D:')
printout(D)
print('Построенная матрица C:')
printout(C)
s1 = 0
s2 = 1
v = 0
#if len(C)%2 != 0:
for c in range(int(len(C)/2)+1):
    for i in range(0+c,len(C)-c):
        if c == 0:
            for j in range(len(C)-1,len(C)):
                if j%2 == 0:
                    s1+=C[i][j]
        else:
            for j in range(len(C)-c-1,len(C)-c):
                if j%2 == 0:
                    s1+=C[i][j]

for c in range(int(len(C)/2)+1):
    for j in range(0+c,len(C)-c):
        if c == 0:
            for i in range(-(len(C)),-(len(C))+1):
                if (i*-1)%2 == 0 and i != 0:
                    s2 *= C[i][j]
        else:
            for i in range(-(len(C))+c,-(len(C))+c+1):
                if i%2 == 0 and i != 0:
                    s2 *= C[i][j]
if s1 > s2:
    for i in range(int(len(C)/2)+1):
        for j in range(int(len(C)/2)+i):
            v = C[i][len(C)-j-1]
            C[i][len(C)-j-1] = C[len(C)-j-1][i]
            C[len(C)-j-1][i] = v
    print('Матрица C после вычислений:')
    printout(C)
    F = [[0 for x in range(n)]for x in range(n)]
    if n % 2 == 0:
        for i in range(int(n/2)):
            for j in range(int(n/2)):
                F[i][j] = E[i][j]
        for i in range(int(n/2)):
            for j in range(int(n/2),n):
                F[i][j] = B[i][j-int(n/2)]
        for i in range(int(n/2),n):
            for j in range(int(n/2)):
                F[i][j] = D[i-int(n/2)][j]
        for i in range(int(n/2),n):
            for j in range(int(n/2),n):
                F[i][j] = C[i-int(n/2)][j-int(n/2)]
    else:
        F = [[0 for x in range(n)]for x in range(n)]
        for i in range(n):
            for j in range(n):
                F[i][j] = A[i][j]
        for i in range(int(n/2)+1,n):
            for j in range(int(n/2)+1,n):
                F[i][j] = C[i-int(n/2)-1][j-int(n/2)-1]
    print('Построенная матрица F:')
    printout(F)
else:
    F = [[0 for x in range(n)]for x in range(n)]
    for i in range(n):
        for j in range(n):
            F[i][j] = A[i][j]
    if n % 2 == 0:
        for i in range(int(n/2)):
            for j in range(int(n/2)):
                v = F[i][j]
                F[i][j] = F[i][j+int(n/2)]
                F[i][j+int(n/2)] = v
    else:
        for i in range(int(n/2)):
            for j in range(int(n/2)):
                v = F[i][j]
                F[i][j] = F[i][j+int(n/2)+1]
                F[i][j+int(n/2)+1] = v
    print('Построенная матрица F:')
    printout(F)
r = MminusM(MonM(MonK(A,k),A),MonK(transpose(A),k))
print('Результат вычислений:')
printout(r)





























