list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]

print(min(list1)) # [1, 7, 12, 0, 9, 100] Минимальным считается тот, у которого первый элемент не совпадающий меньше
print(max(list1)) # [1, 10] Аналогично для поиска максимального
print(min(list2)) # ['a'] Со строками также, по значению чара
print(max(list2)) # ['d', 'p', 'q']

my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]

# print(min(my_list)) # TypeError: '<' not supported between instances of 'str' and 'int'
# print(max(my_list)) # TypeError: '<' not supported between instances of 'str' and 'int'

list1 = [[0, [9, 2]], [1, [4, 6, 3], [5, 2, 3], 8, 3]]
print(list1[1][2][1])

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)