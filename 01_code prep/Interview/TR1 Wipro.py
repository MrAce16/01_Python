import schedular
import db

def optimize_large_response():
    with db_connection as conn:
        cursor = conn.cursor()

        cursor.execute ("SELECECT id, response from responses where LENGTH(response) > 2000")
        records = cursor.fetchall()

        #for record in records:

        cursor.execute = ("UPDATE response SET  response = %s where id = %s", (new_txt, record['id']))
        conn.commit()

        schedule.every().min.at("00:02").do(optimize_large_responses)

        while True:
            schedule.run_pending()
            time.sleep(120)
            



#db -collections - record(tokens: 5000)


from itertools import count 
iterator =(count(start = 0, step = 2)) 
print(list(next(iterator) for _ in range(5))  # output = 0,2,4,6,8


my_list =["Fname", "Lname", "Location"] 
for i in zip(count(start = 1,step = 1), my_list):
    print(i)   # output = Fname : 1, Lname : 2, Location : 3