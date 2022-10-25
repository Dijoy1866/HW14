# Задание 1
#Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в
#списке. Position всегда должен быть последовательным, например у нас есть список
#Придерживаясь такой логики, необходимо реализовать:
# Удаление элемента

from pprint import pprint

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4},
    {'name': 'Test 5', 'position': 5}
]

def delete_pos(lst, position_number):
    lst.pop(position_number - 1)
    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


pprint(delete_pos(data, 2))


