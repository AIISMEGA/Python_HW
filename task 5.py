from functools import reduce


def checklist(num_1, num_2):
    return num_1 * num_2


final_list = [num for num in range(100, 1001, 2)]

print(reduce(checklist, final_list))

