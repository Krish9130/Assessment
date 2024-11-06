# Sort a list of tuples by the second element in each tuple

# Sample list of tuples
my_list = [(1, 'git'), (2, 'docker'), (3, 'Ansible'), (4, 'Ansible')]

# Sorting by the second element
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)


