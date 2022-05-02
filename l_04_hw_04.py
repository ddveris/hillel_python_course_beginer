#Задача 2
text = 'Hillel school'
import collections
print(dict(collections.Counter(text)))

#Задача 4
x = input('your name')
z = '{},{}'.format(x.upper(), x.lower())
print(z)

#Задача 5
x = input('Введите Ваши любимые цвета:')
user_list = x.split(',')
y = list(set(user_list))
z = sorted(y)
print(z)

#Задача 7
#Насколько я понимаю, есть несколько вариантов
y = input('Введите данные:')
lst = [x for z in y for x in z]                    #Первый
#lst = [*y]                                         #Второй
print(lst)

#Задача 8
x = list(range(-99,99,3))
#for i in x:                                  Этот способ выводит те же числа, что и range
    #if(i%3==0):
        #print (i)
print(f'Это {x}\n делиться без остатка на 3.')

 # Задача 6
x = input('Числа: ')
x = list(x)
# y = int(len(x/3))
x.remove('3') and x.remove(',')
x = tuple(x)
# b.append(x)
print(x)


#Задачи, которые не получились:
#Задача 3
x = input("Shoplist: ")
#y = ['{}'].format(x)
#y = [_,{}].format(x)
#x = ['bread', 'milk', 'kolbasa']
#sl : str = ['bread', 'milk', 'kolbasa']
#sl1 = f'str, {sl}'
#''.format(x)
print(max(x, key=len))

#Задача 1
str2 = 'Ваша строка слишком короткая - %s'%('Hillel school')
str1 = 'Ваша строка слишком короткая - %s'
x = 'Hillel school'
if len(x) > 2:
    print('Hillel school'[0: 2][-1: -2])
elif len(x) < 2:
    print('Ваша строка слишком короткая - %s'%(str))



#Задача 9
for x in [1, 2, 3]:
    if x == [3, 4, 5]:
        print(x)