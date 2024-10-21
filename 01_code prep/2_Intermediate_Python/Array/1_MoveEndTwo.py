def move_twos_to_end(arr):
    # List of elements that are not 2
    non_twos = [x for x in arr if x != 2]
    # List of elements that are 2
    twos = [x for x in arr if x == 2]
    # Combine the lists
    return non_twos + twos


# Example usage
arr = [1, 2, 3, 2, 4, 5, 2]
result = move_twos_to_end(arr)
print(result)
