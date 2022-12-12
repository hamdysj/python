from nltk.tokenize import sent_tokenize, word_tokenize
from corpuss import store, tables, dept, values
from Apps.entry import cur_db, con_db

from Apps import entry

text = "Show me all the students that has paid in arabic"
text_token = word_tokenize(text)

# Map word to corresponding word
nlq = []
for word in text_token:
    text_lower = word.lower()
    if text_lower in store.keys():
        nlq.append(store[text_lower])
    else:
        nlq.append('')

print(nlq)
table = ''
column_name = ''
value = ''

# Extract table names
for word in nlq:
    if word in tables.keys():
        if word == "students":
            table = tables[word]
        elif word == "paid" or word == "payment":
            table = tables[word]
        else:
            table = tables[word]


# Extract column names
for word in nlq:
    if word in dept.keys():
        column_name = dept[word]


# Extract the value
for word in nlq:
    if word in values.keys():
        value = values[word]

# sql1 = f'select * from {table} where {column_name} = {value}'
if column_name != '':
    sql1 = "select * from " + table + " where " + column_name + " = " + value
else:
    sql1 = "select * from " + table

print(sql1)