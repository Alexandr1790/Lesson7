             #Словари
my_dict = {'Urban': 718273128, "Mikhail": 12312478}
print(my_dict)
print(my_dict.get('Urban'))
my_dict['Alex'] = 234567876
print(my_dict.get('Alex'))
my_dict.update({'Loli': 63789223, 'Kasi': 3245432343})
a = my_dict.pop('Loli')
print(my_dict)
print(a)
print(my_dict)
               #Множества
my_set = {1, 2, 3, 1, 2, 3, False, 'Apple'}
print(my_set)
my_set.add('8, 5')
print(my_set)
my_set.discard(1)
print(my_set)