def find_indices_in_range(arr, min_value, max_value):
    indices = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indices.append(i)
    return indices

my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, -8, 10, -9, 0, -5, -5, 7]
min_value = 10
max_value = 25

result = find_indices_in_range(my_list, min_value, max_value)
print("Индексы элементов в диапазоне:", result)
