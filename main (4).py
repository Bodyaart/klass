#coding utf-8:
dark=input("Вы хотите спать(да, нет, не знаю)")
if dark == "Да":
    print("Идите спать")
elif dark == "не знаю":
    print('подумайте еще')
else:
    print('Идите гулять')
    
#задача #1 
one=input("1 Больше нуля(да, нет, не знаю)")
if one == "Да":
    print('значит меньше чем ноль')
elif one == "не знаю":
    print('подумай')
else:
    print('Значит больше нуля')

#задача 2
zero=input("Больше 0, меньше 0")
if 0>1 == "Больше":
    print("-1")
elif zero == "не знаю":
    print("Думай еще")
else:
    print("1")

#Задача 3
peremenye=input("меньше,больше(1,2)")
if peremenye == "1":
    print(1-2)
elif peremenye == "не знаю":
    print("решай")
else:
    print(1+2)
    
#Задача 4 часть б
arbuz=input("арбуз больше чем дыня (да, нет, не знаю")
if arbuz == "Да":
    print("ВСМЫСЛЕ")
elif arbuz == "не знаю":
    print("круто, я тоже")
else:
    print("РЕАЛЬНО БОЛЬШЕ")