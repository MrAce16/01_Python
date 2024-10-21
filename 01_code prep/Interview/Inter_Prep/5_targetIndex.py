
# list2 = [4,6,9,13,18]
# target = 7
# output_index=2

def find_insert(list2, target):

    # if target > len(list2):
    #     return f"Index {target} is out of range. This list length is {len(list2)}"

    for i in range(len(list2)):
        if target <= list2[i]:
            return i


list2 = [4, 6, 9, 13, 18]
target = 7
output_index = find_insert(list2, target)
print(f"target {target} would fit at index : {output_index}")
