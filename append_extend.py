# 1. append(item): Adds item as a single element to the end of the list.

# Using append
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)  # Output: [1, 2, 3, [4, 5]]


# 2. extend(iterable): Adds each element of an iterable (e.g., another list) to the end of the list.

# Using extend
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


