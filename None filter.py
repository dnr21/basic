random_list = [10, 'b', 0, False, True, '0']
filtered_iterator = filter(None, random_list)
filtered_list = list(filtered_iterator)
print(filtered_list)
