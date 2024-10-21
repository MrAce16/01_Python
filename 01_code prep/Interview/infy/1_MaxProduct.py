def max_product(arr):
    a_len = len(arr)
    if a_len < 2:
        print("No such pair exist")
        return
    a = arr[0]
    b = arr[1]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] * arr[j]) > (a*b):
                a = arr[i]
                b = arr[j]
    return a, b


arr = eval(input("Entery the array: "))
print(f"max product of array is {max_product(arr)}")
