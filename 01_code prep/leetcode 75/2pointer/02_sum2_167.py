# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].



def TwoSum(numbers,target):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target :
                print(f"{i},{j}")
                break


numbers = [2,7,11,15]
target = 17
solution = TwoSum(numbers,target)
print(solution)
