#coding utf-8
#Задача 1 
c=int(input("Введите количество чисел: "))
a=0
b=1 
print(a)
print(b)
i=0 
while i<=c:
    sum = (a+b)
    print(sum)
    i += 1 
    a=b 
    b=sum
#Задача 2
num = 0
while num <=20:
    print(num)
    num +=2
    
num =-1
count = 0 
while num >= -21:
    if count %3 == 0:
        print(num)
        num -=1 
        
#Задача 3
i = 0 
while i < 5:
    print("Привет мир")
    i += 1
