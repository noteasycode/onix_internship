matrix = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]

# first task
sorted_array = []
for i in range(len(matrix)):
    sorted_array.append(matrix[i][1])
sorted_array.sort()
print(sorted_array)

# second task
for i in range(len(matrix)):
    del(matrix[i][1])
dict_from_matrix = dict(zip(sorted_array, matrix))
print(dict_from_matrix)

# third task
sorted_dict = {key: sorted(
    dict_from_matrix[key], reverse=True
) for key in sorted(dict_from_matrix)}
print(sorted_dict)

# fourth task
set_from_dict_values = set()
for i in sorted_dict.values():
    set_from_dict_values.update(i)
print(set_from_dict_values)

# fifth task
set_to_str = ", ".join(map(str, set_from_dict_values))
print(type(set_to_str))
print(set_to_str)
