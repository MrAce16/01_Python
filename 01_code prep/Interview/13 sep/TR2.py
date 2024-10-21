str = "helloworld"

dict1 = {}
for i in str:
    if i  in dict1:
        dict1[i] +=1
    else:
        dict1[i] = 1
print(dict1)

'''sql inner join :

    select orders.order_id,
    customers.customer_name
    From orders
    INNER JOIN CUSTOMERS ON orders.custer_id= customers.customer_id;

    LEFT JOIN :

    select orders.order_id,
    customers.customer_name
    From orders
    LEFT JOIN CUSTOMERS ON orders.custer_id= customers.customer_id;

    RIGHT JOIN :

    select orders.order_id,
    customers.customer_name
    From orders
    RIGHT JOIN CUSTOMERS ON orders.custer_id= customers.customer_id;


    FULL OUTER JOIN :

    select orders.order_id,
    customers.customer_name
    From orders
    FULL OUTER JOIN CUSTOMERS ON orders.customer_id= customers.customer_id;

    self join:

    select e1.employee_id , e1.first_name,
    e2.first_name AS manager_name

    INNER JOIN  employees e2 on e1.manager_id'''
