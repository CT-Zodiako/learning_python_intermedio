#Lists array
my_list = list();
my_other_list = [];

print(type(my_list))
print(my_list)
my_list = [1,'a',2,'b',1]

print(my_list[::-1])
print(my_list[0:3:])
print(my_list[1:3])

my_other_list = [1,2,3,4,5]

add = my_other_list + my_list
print(add)

print(add.count(1)) #cuenta las ocurrencias que hay del  parametro shearch

one , two , three, *rest = add
print(one , two , three, rest)

my_list.append('Nuevo')
my_list.insert(0, 'Otro')

print(my_list)

my_list.remove('Otro')
my_list.remove(my_list[0])
my_list.pop();
my_list.pop(0);

print(my_list.pop())
print(my_list)

del my_list[0]
print(my_list)

my_list.clear()

print(my_list)




