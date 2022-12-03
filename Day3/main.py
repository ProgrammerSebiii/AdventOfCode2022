import functools

f = open("rucksacks.txt","r")
all = []

num_dict = {}
start_char = 'a'
for num in range(1, 27):
    num_dict[start_char] = num
    start_char = chr(ord(start_char) + 1)

start_char = 'A'
for num in range(27, 53):
    num_dict[start_char] = num
    start_char = chr(ord(start_char) + 1)

for line in f.readlines():
    line = line.replace("\n","")
    items = list(line)
    num_items = len(items)
    half_items = items[0:round(num_items/2)]
    second_hlaf_items = items[round(num_items/2):]
    items_in_both = []
    already_compared = []
    for item in half_items:
        if item in second_hlaf_items and item not in already_compared:
            items_in_both.append(num_dict[item])
            already_compared.append(item)
    for item_in_both in items_in_both:
        all.append(item_in_both)
print(sum(all))


def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list


f = open("rucksacks.txt")
groups = []
current_group = []
for line in f.readlines():
    line = line.replace("\n","")
    if len(current_group) == 3:
        current_group = []

    unique_list = unique(list(line))
    unique_item_str = functools.reduce(lambda x, y: x + y, unique_list)
    current_group.append(unique_item_str)
    if len(current_group) == 3:
        groups.append(current_group)
print(groups)

group_batches = []
for group in groups:
    group1, group2, group3 = group
    for item in group1:
        if item in group2 and item in group3:
            group_batches.append(num_dict[item])
            break

print(sum(group_batches))

