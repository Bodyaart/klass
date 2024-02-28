#coding utf-8
#Задача 2
A = int(input("введите число A "))
B = int(input("Введите число B "))

if A < B:
    for i in range(A + 1, B):
        print(i)
else:
    print("Ошибка A должно быть меньше B")
    
#Задача 3
A = int(input("Введите число A "))
B = int(input("Введите число B "))

if A < B:
    for i in range(B - 1, A - 1):
        print(i)
else:
    print("Ошибка A должно быть меньше B")
    
#Задача 4
N = int(input("Введите целое число N(>1): "))

K = 1 
while 3*K <= N:
    K += 1 
print("Наименьшее целое K, при котором выполняется равенство 3K > N и само значение 3K:", K)
#Задача 5
N = int(input("Введите целое число N(>1): "))

K=1
while 3*K <= N:
    K += 1
    
K -= 1
print("Наибольшее целое K, при котором выполняется равенство 3K < N и само значение 3K:", K)

#Задача 6
N = int(input("Введите натураульное число N: "))

if N <= 0:
    print("Введите положительное  натураульное число")
else:
    i = 1:
        while i < N:
            print(i)
            i += 1

if N <= 0:
    print("Введите положительное натуральное число")
else:
    for i in range(1,N):
        print(i)
