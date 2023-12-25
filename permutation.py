def permutations(list1):
    if len(list1) == 0:
        return []
    if len(list1) == 1:
        return [list1]
    l = []
    for i in range(len(list1)):
        m = list1[i]
        remList = list1[:i] + list1[i+1:]
        for p in permutations(remList):
            l.append([m] + p)
    return l

my_list = [1, 2, 3]
all_permutations = permutations(my_list)
print("Original List:", my_list)
print("All Permutations:", all_permutations)
