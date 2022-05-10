#Задача 1 Задачу по заданным условиям решил, но подозреваю,
# что есть более короткий способ решения
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
common = dict()
for key,value in first.items():
    common[key] = value
for key,value in second.items():
    common[key] = value
for key,value in third.items():
    common[key] = value
for key,value in fourth.items():
    common[key] = value
for key,value in fifth.items():
    common[key] = value

print(common)

#Задача 2
d = dict()
for x in range(11,21):
    d[x] = x**2
print(d)
print(sum(d.values()))

#Задача 3 Испробовал разные разные способы,
# почему-то не все работают, хотя версия пайтона выше 3.7
d = {
    'Superman' : 'Metropolis',
    'Betman' : 'Gotham',
    'Aquaman' : 'Atlantis',
    'Flash' : 'Central City'
}
sd = sorted(d.items())
for k,v in sd:
    print(k,v)

#Задача 5
# Задачу решил, но с ошибкой. При распаковке списка в словарь теряются
# не уникальные ключи(понимаю, что это особенность словаря, но решить проблему не смог).
# Подскажи, как выйти из ситуации.
dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
result = {}
for d in dict_list:
    result.update(d)
uniqueValues = set(result.values())
print(uniqueValues)


#Ссылка документацию по словарям
https://docs.python.org/3/search.html?q=dict&check_keywords=yes&area=default

#                           Задачи, которые не получились
#Задача 4
#Пробовал двумя способами, но не получилось
list = {
'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}},
'id3':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}}
}
#new_list = ({v['id']:v for v in list}.values())
#new_list = [dict(s) for s in set(frozenset(d.items()) for d in list)]
print(new_list)


#Задача 6
# В этой задаче застопорился, когда программа не захотела подсчитывать None присвоить другое значение смог.
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
x = list(dict.values(shedule))

#y = []
#for i in x:
    #for item in i:
        #y.append(item)

#for item in enumerate(y):
    #if item == None:
        #item[y] = 0
#print(x)
print(len(x))