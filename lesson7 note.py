                       #Словари
phone_book = {'Denis': 79930861895, 'Max': 88923829349} # Словарь, работает только во множественном числе и может изменяться!
print(phone_book['Denis'])
phone_book['Anton'] = 8172408108 #Добавление нового значения
del phone_book['Max']
phone_book.update({'Sasha': 32849384730, 'Pasha': 9832783}) #Добавление сразу нескольких пар
print(phone_book)
print(phone_book.get('Denis')) # Вывести на экран 1 пару
print(phone_book.get('Antoni', 'Note keys')) #Если нету такой пары, тогда напишет "None", но это значение можно изменить если через запятую написать новый текст
a = phone_book.pop('Denis')
print(phone_book)
print(a)
print(phone_book.keys()) #Достает имена
print(phone_book.values()) #Достает значения
print(phone_book.items()) #Возвращает сразу парами
                         #Множества
set_ = {1, 2, 3,4 ,5 , 1, 2, 3, 4, 'String', True, (1, 2, 3, 3)}
print(set_) #Хранит в себе любые данные и не повторяет 1 значение несколько раз
lol = [1, 1, 2, 2, 1, 4, 3]
print(lol)
print(lol.remove(1))
print(lol)
print(lol.add(5))#Добавление элементов во множестве
