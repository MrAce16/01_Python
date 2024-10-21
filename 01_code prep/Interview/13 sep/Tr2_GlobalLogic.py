# The problem involves placing N queens on an N x N chessboard 
# so that no two queens threaten each other.
# Out put will be based on the n values 
# for 4 it should be 
# [0, 0, 1, 0]
# [1, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 1, 0, 0]
# logic : n = 4 
# def n_queen2(row,col,n,board):

#     for i in range(row):
#         if board[i] == col:
#             re

# def n_queen1(n):
#     pass


# n = 7
# solution = n_queen1(n)
# print(solution)

# def reverse_temp(temp):
#     if temp < 0:
#         return -reverse_temp(-temp)
    
#     num = 0
#     while temp > 0:
#         num = num *10 + temp % 10 
#         print(num)
#         temp = temp//10
#     return num

# temp = -123
# reverse= reverse_temp(temp)
# print(reverse)

#output = ["Ramesh", "Kiran", "RAM", "RaJ"]

college = [{
    "branch":{
        "depet":{
            "section":{
                "name":"Ramesh",
                "sir_name": "R"
            }
        }
    },
    "section1":
        {
            "name":"Kiran",
            "sir_name": "M"
        }
},
{
    "branch":{
        "depet":{
            "section":{
                "name":"RAM",
                "sir_name": "S"
            }
        }
    },
    "section1":
        {
            "name":"RaJ",
            "sir_name": "RR"
        }
}]
output = []
for i in college:
    
    name1 = i["branch"]["depet"]["section"]["name"]
    name2 = i["section1"]["name"]
    output.append(name1)
    output.append(name2)

print(output)

    

