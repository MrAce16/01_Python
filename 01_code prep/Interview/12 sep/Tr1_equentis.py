'''1. We need a list of tuples in descending order of occurrence [(the, 5), (in, 3), (of, 3)...]
2. If two or more words have the same occurrence they should be sorted alphabetically.
3. You need to ignore the case of every word.(The, the, THE are all considered the same
word)
4. All non alphanumeric characters are replaced with a space “ “ in the original string.
5. Also print the list of pages the random page provided to check the output.
6. You are expected to create a python virtual environment and install relevant libraries.'''

import requests
import re
import urllib.request


# def exact_data():
#     #text = text.


def get_wiki_data():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(response.url)
        return data.get('extract','')
    else:
        return None
def word_count(input_string):
    dict1 = {}
    str1= input_string.lower()
    str1 = re.sub('[^a-zA-Z0-9 ]', ' ', str1)
    
    for i in str1.split(' '):
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    sorted_count = sorted(dict1.items(), key =lambda x:(-x[1], x[0]) )
    # sorted_count= sorted_count.lower()
    print(sorted_count)

# str1 = '''Evander Holyfield vs. Vitor Belfort billed as "No Holds Barred", was an exhibition boxing match between former undisputed heavyweight world champion Evander Holyfield and former UFC light-heavyweight champion Vitor Belfort on September 11, 2021, at the Seminole Hard Rock Hotel & Casino Hollywood in Miami, Florida. Belfort won the fight by TKO at 1:49 of the first 
# round. The fight sold 150,000 PPV buys'''

for i in range(10):
    word_count(get_wiki_data())


#2. If two or more words have the same occurrence they should be sorted alphabetically.
# sorted_count = sorted(dict1.items(),keys =lambda x:(-x[1], x[0]) )

# print(get_wiki_data())


