'''
Неправильные горы
Ограничение времени	1 секунда
Ограничение памяти	64.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
При путешествии по планете марсоход постоянно замеряет высоту рельефа и сохраняет результаты замеров в массив.

Одна из задач марсохода — поиск «правильных гор». «Правильной» считается та гора, у которой на пути от подножия до вершины высота постоянно растёт, а на пути от вершины к подножию — постоянно уменьшается. Если у горы есть несколько вершин или в каком-то месте встречается горизонтальный участок — это «неправильная гора».

Напишите функцию valid_mountain_array, которая будет принимать на вход массив с высотами и возвращать True или False в зависимости от того, «правильная» это гора или нет.

Если в массиве менее трёх элементов, такой массив не может описывать «правильную» гору.

'''
def is_right_mountain(arr):
    i_of_max = arr.index(max(arr))
    return i_of_max not in (0, len(arr) - 1) and (all(R - L > 0 for (L, R) in zip(arr[:i_of_max], arr[1:i_of_max + 1]))
                                                  and all(
                R - L < 0 for (L, R) in zip(arr[i_of_max:], arr[i_of_max + 1:])))


*arr, = map(int, input().split())
print(is_right_mountain(arr))
