def animal(func):
    def wrapper():
        print("hello python")
        func()
        print("hello python 1")
    return wrapper

@animal
def dog():
    print("this is dog function")

dog()

# iter 
# list = [1,2,3,4]

# iter1 = iter(list)

# print(next(iter1))

# import requests

# url = "https://abc.com/api"
# data ={
#     'name' : 'john'
#     'email' : 'abc@abc.com'

# }

# response = requests.post(url, json = data)

# if response.status_code == 200:
#     print("success")
#     print(response.json())

# else:
#     print("failed to post data",response.status_code)
# # how api function

# from django.db import models

# class data(models.model):
#     name = models.CharField(max_length= 100)
#     description = models.TimeField()



# @api_views(['post'])
# def data_list(request):
#     if request.method == 'POST':
#         searli


