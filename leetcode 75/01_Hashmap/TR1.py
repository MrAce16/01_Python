#  import requests

# class task:
    

#     def post(self):
#         data = requests.get_json()
#         task = task(title = data["title"])
#         db.session.add(task)
#         db.session.commit()
#         return jsonify (task.json()) , 200
    
#     def delete(self, task):
#        task = task.query.get()
#        db.session.delete(task)
#        db.session.commit()
#        return jsonify ("task deleted")


#Given an unsorted list of integers, write a Python function to find the kth largest element without using any built-in sorting functions

# 
def partiton(arr,low, high):
    p = arr[high]
    i = low -1

    for j in range(low,high):
        if arr[j] >= p:
            i +=1
            arr[i],arr[j] = arr[j], arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1

def quickS(arr,low,high,k):
    if low <= high:
        pi = partiton (arr,low,high)
        if pi ==k:
            return arr[pi]
    elif pi > k:
        return quickS(arr,low, pi-1, high,k)
    else:
        return quickS (arr, pi+1, high, k)
    return -1
def find_kth_largest(arr,k):
    n = len(arr)
    return quickS(arr,0,n-1,k-1)
    
arr =[3,2,1,5,6,4]
k = 4
print(f"{k} largest element is {find_kth_largest(arr,k)}")



