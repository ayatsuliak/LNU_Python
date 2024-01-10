import sys
# sys.stdin.readline()
# sep=""  в прінт виводить без пробілів
# end=""
# round = заокруглення
# rstrip() - идаляє пробіли і ентери з кінця
# // ділить націло

# test_file = open('d:\\test.txt')
# text = test_file.read()
# print(text)
# test_file = open('d:\\test.txt', 'w')
# test_file.write('thanks, i\'m fine')
# test_file.close()

# class Animal:
#     def __init__(self, value, count, color):
#         self.value = value
#         self.count = count
#         self.color = color
#
# Garri = Animal('gipo', 6, 'pink')
# import copy
# Garriest = copy.copy(Garri)
# my_animal = [Garriest, Garri]
# more_animal = copy.copy(my_animal)
# print(more_animal[1].color)
# # copy.deepcopy - копіює повністю список(конкретний параметр)
#
# sys.stdout.write("Whats your name?")
# v = sys.stdin.readline()
# print(v)

# import pickle
# file = open('favorites.dat', 'wb')
# my_list = ['football', 'baskatball', 'borshch']
# pickle.dump(my_list, file)
# file.close()
#
# new_file = open('favorites.dat', 'rb')
# my_new_list = pickle.load(new_file)
# print(my_new_list)
# new_file.close()

# nums = [5, 3, 5, 6]
# nums[-1] #last elem
# nums.append(100) додає в кінець нове число
# nums.insert(1, True) добавляє новий елем на індекс вказаним першим
# nums.extend([5,4,3]) добавляє новий список в кінець поточного списку
# nums.remove(5) видаляє число 5
# word = 'hello'
# word.upper() робить всі букви великими або word.lower()
# word.capitalize() перша буква з великої
# word.split() розділяє слово за певним символом
# word.join() зєднує знову в строку

# tuple() - ф-ція, яка переводить список в кортедж

# try:
#     x = int(input("Enter number: "))
#     x += 5
#     print(x)
# except ValueError:
#     print("Enter number please: ")
# finnaly:
#      don't know what a mistake

# import webbrowser
#
# def validator(func):
#     def wpapper(url):
#         if '.' in url:
#             func(url)
#         else:
#             print('Mistake in your URL')
#     return wpapper
#
# @validator #декоративна ф-ція
# def get_url(url):
#     webbrowser.open(url)
#
# get_url("https://translate.google.com")

# a, *val, b =[1, 2, 5, 2, 6 ] # а і b приймають крайні знач, а середні знач *val
# a = [2]
# b, = a #розпаковує знач а
#
# import random
# a = [random.randint(0, 9) for _ in range(20)]  #рандомний список 20 чисел

# (a, b)[c] виведеться елем з ондексом с

# ord(char) - повертає номер букви

# def solution(number):
#     sum = 0
#     for x in range(number):
#         if x % 3 == 0 or x % 5 == 0:
#             sum += x
#     return sum
#
#
#
#
# def funct(value):
#     match value:
#         case 400:
#             return "Yes"
#         case 450:
#             return "No"
#
# print(funct(400))
#
#
#
# import numpy
#
# def func(value):
#     return numpy.sum(numpy.arange(value))
# print(func(11))


# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
# print([[row[i] for row in matrix] for i in range(4)])
# # print(17//3) - повертає цілу частину від цілого
# print(complex(5, 2))
#
# def palindrom(string):
#     if str(string) == str(string)[::-1]:
#         print('Yes')
#     else:
#         print('No')
# #перевірити половину коду
#
#
# word = str(input('Enter word: '))
# palindrom(word)


# up = tuple()
# print((0, 1, 20) < (0, 3, 4))


# my_list = ['Yatsuliak Andriy', 'Jenchenko Oleksandr', 'Protskiv Nazarii', 'Goshko Sofia']
# dict_from_my_list = {}
# for i in my_list:
#     elem = str(i)
#     name_and_surname = elem.split(' ')
#     surname = name_and_surname[0]
#     name = name_and_surname[1]
#     dict_from_my_list[surname] = name
# print(dict_from_my_list)



# dict_of_grouplist = {'Borovets':'Roman', 'Brezin':'Anton', 'Hatala':'Olena', 'Hoshko':'Sofiia', 'Hranovskyy':'Dmytro', 'Zhenchenko':'Oleksandr', 'Zelenko':'Iryna', 'Ishchuk':'Andriy',
#                  'Kaparys':'Andriy', 'Krynytskyy':'Maksym', 'Kurka':'Victoriia', 'Linnik':'Vladyslav', 'Masnyk':'Anastasiia', 'Matiash':'Sviatozar', 'Padalka':'Mariia', 'Pik':'Andriy',
#                  'Protskiv':'Nazarii', 'Skvarko':'Andriy', 'Stets':'Rostyslav', 'Tutko':'Volodymyr', 'Shafran':'Olena', 'Iatsuliak':'Andriy'}
#
# vowels = 'AaEeIiOoUu'
# vcount = 0
# dict_of_names_and_vcounts = {}
#
# for i in dict_of_grouplist:
#     # print(type(i))
#     for j in dict_of_grouplist[i]:
#         if j in vowels:
#             vcount += 1
#     print(vcount)
#     dict_of_names_and_vcounts.update({dict_of_grouplist[i]:vcount})
#     vcount = 0
#
# max_keys = [key for key, value in dict_of_names_and_vcounts.items() if value == max(dict_of_names_and_vcounts.values())]
# sorted_keys = [key for key, value in dict_of_names_and_vcounts.items() if value >= value + 1 ]
# max_value = max(dict_of_names_and_vcounts.values())
# print("People who have max count of vowels in name: ", max_keys, "\nCount of vowels in name: ", max_value)
##############################
# def sort_by_vowels(students):
#     return {k: v for k, v in sorted(students.items(), key=lambda item: -count_vowels(item[1]))}
#
# students = {'Borovets':'Roman', 'Brezin':'Anton', 'Hatala':'Olena', 'Hoshko':'Sofiia', 'Hranovskyy':'Dmytro', 'Zhenchenko':'Oleksandr', 'Zelenko':'Iryna', 'Ishchuk':'Andriy',
#                  'Kaparys':'Andriy', 'Krynytskyy':'Maksym', 'Kurka':'Victoriia', 'Linnik':'Vladyslav', 'Masnyk':'Anastasiia', 'Matiash':'Sviatozar', 'Padalka':'Mariia', 'Pik':'Andriy',
#                  'Protskiv':'Nazarii', 'Skvarko':'Andriy', 'Stets':'Rostyslav', 'Tutko':'Volodymyr', 'Shafran':'Olena', 'Iatsuliak':'Andriy'}
# print(id(students))
#
# def count_vowels(word):
#     sum = 0
#     for x in word:
#         if x.lower() in "aeuio":
#             sum += 1
#     return sum
#
# students = sort_by_vowels(students)
# print(id(students))
# for surname, name in students.items():
#     print(surname, name, end=": ")
#     print(count_vowels(students[surname]))



#list1 = [['k', 'a', 'k', 'a', 'k'], ['k', 'a', 'k']]
# def func(_list):
#     vowels = "AaEeOoYyIiUu"
#     lens = 0
#     size = len(_list)
#     new_list = []
#     for i in range(size):
#         our_list = _list[i]
#         if len(our_list) > lens:
#             lens = len(our_list)
#             if (our_list[0] in vowels) and (our_list[-1] in vowels):
#                 continue
#             else:
#                 new_list.append(our_list)
#
#     return new_list
#
# print(func(list1))


# lol = [['a', 't', 'b', 'r'], ['a', 'y', 'e'], ['r', 'a', 't', 'o', 'j', 'i', 'k'], ['t', 'c', 'o']]
# def func(_list):
#     vowels = "AaEeOoYyIiUu"
#     size = len(_list)
#     new_list = []
#
#     for i in range(size):
#         start = []
#         our_list = _list[i]
#         size2 = len(our_list)
#         for j in range(size2):
#             if our_list[j] not in vowels:
#                 start.append(j)
#             else:
#                 continue
#
#         new_list.append(start)
#         list_finish = []
#         for k in range(size):
#             our_list = _list[k]
#             size2 = len(our_list)
#             for m in range(size2):
#                 if len(new_list) == 1:
#                     first = new_list[0]
#                     list_finish.append(our_list[first])
#                 else:
#                     first = new_list[0]
#                     last = new_list[-1]
#                     list_finish.append(our_list[first:last])
#
#
#     return list_finish
#
#
# print(func(lol))




