import sys

def quicksort(array):
    """Быстрая сортировка."""
    len_array = len(array)

    # Базовый случай рекурсии.
    if len_array <= 1:
        return array
    # Определяем индекс опорного элемента.
    middle_element_index = len_array // 2
    # Получаем опорный элемент:
    pivot = array[middle_element_index]
    # Передаём в функцию partition() массив и опорный элемент.
    left, center, right = partition(array, pivot)
    # Рекурсивно вызываем quicksort() для левого и правого списков, 
    # а затем соединяем все три списка в один.
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    """
    Разбивает массив на три разных массива относительно опорного элемента.
    """
    # Создаём три пустых списка.
    left, center, right = [], [], []
    # Раскладываем элементы по спискам.
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    # Возвращаем кортеж с тремя списками.
    return left, center, right


orders_size = int(sys.stdin.readline().rstrip())
orders = sys.stdin.readline().rstrip().split()
orders = [int(item) for item in orders]
# orders = [8, 2, 4, 7, 8, 5, 5, 8, 6, 9]
orders = quicksort(orders)
# stock = [9, 8, 1, 1, 1, 5, 10, 8, 2, 7, 4, 3, 15]
stock_size = int(sys.stdin.readline().rstrip())
stock = sys.stdin.readline().rstrip().split()
stock = [int(item) for item in stock]
stock = quicksort(stock)
pointer = 0
count = 0
for item in stock:
    if pointer == len(orders):
        break
    if item >= orders[pointer]:
        pointer += 1
        count += 1
print(count)
