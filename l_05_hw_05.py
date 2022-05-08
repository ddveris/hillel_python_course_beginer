#Задача 1
x = input('Password:')
y = input('Repeat password:')
if x == y:
    print('Accepted')
else:
    print('Incorrect password, try  again')

#Задача 2
x = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
while 'eg' in x:
    x.remove('eg')
print(x)

#Задача 3
x = [11, 23, 65, 44, 76, 533]
i = 0
z = len(x)
while i < z and x[i] % 2 == 0:
    print("all numbers are even")
    break
else:
    print('No')

#Задача 4  Эта задача не получилось, подскажи пжлст как решить.
x = dir(set)
x = list(x)
x.remove('_ _')
print(x)

#Задача 6
a = {1, 2, 3}
b = {2, 3, 4}
# Union
a.union(b)
{1, 2, 3, 4}
#Intersection
a.intersection(b)
{2, 3}
#Difference
a.difference(b)
{1}
#symmetric_difference
a.symmetric_difference(b)
{1, 4}
#isdisjoint
a.isdisjoint(b)
False
#issubset
a.issubset(b)
False
#issuperset
a.issuperset(b)
False
#update
a.update(b)
{1, 2, 3, 4}
#intersection_update
a.intersection_update(b)
{2, 3}
#symmetric_difference_update
a.symmetric_difference_update(b)
{1, 4}
#add
a.add(6)
{1, 2, 3, 6}
#remove
a.remove(1)
{2, 3}
#discard
a.discard(4)
-
#pop
a.pop()
1
a
{2, 3}
#clear
a.clear()
set()
#copy
a.copy(z)
{1, 2, 3}
#difference_update
a.difference_update(b)
{1}