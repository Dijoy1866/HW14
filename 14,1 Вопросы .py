"""ВОПРОС"""
''' почему при 3 словарях в етой задаче не срабатывает pprint
А при 4 и более работает ?? а в других задачах работает'''

from pprint import pprint
data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    #{'name': 'Test 4', 'position': 4},
    #{'name': 'Test 5', 'position': 5},

]


def delete_pos(lst, position_number):
    lst.pop(position_number - 1)
    for i, i_value in enumerate(lst):
        i_value['position'] = (i + 1)
    return lst


pprint(delete_pos(data, 2))



