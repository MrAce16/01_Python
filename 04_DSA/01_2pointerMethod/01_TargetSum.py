from array import *

arr1 = array("i",[1,4,5,8,34,45])
arr = sorted(arr1)
target_sum = 42

low,high = 0, len(arr)-1
current_sum = 0

while low < high :
    current_sum = arr [low] + arr [high]
    if current_sum == target_sum:
        print(f"found target sum {target_sum} at {arr[low]}, {arr[high]}")
        break
    elif target_sum > current_sum :
        low +=1
    else:
        high -=1
else:
    print("not found an element")