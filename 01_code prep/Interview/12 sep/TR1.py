import pypdf
import re

with open('xyz.pdf','rb') as file:
    reader = pypdf2.pdfreader(file)
    text = ''
    for page in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extact-text()
    print(text)

    pattern


