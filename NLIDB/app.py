from nltk.tokenize import sent_tokenize, word_tokenize
from corpuss import store, tables, dept, values
from Apps.entry import cur_db, con_db

from Apps import entry

text = "What is the health status of all students"
text_token = word_tokenize(text)

# Map word to corresponding word
nlq = []
for word in text_token:
    text_lower = word.lower()
    if text_lower in store.keys():
        nlq.append(store[text_lower])
    else:
        nlq.append('')

# Extract table names
for word in nlq:
    if word in tables.keys():
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
sql1 = "select student_id, name, level from " + table + " where " + column_name + " = " + value

cur_db.execute(sql1)
cursor = cur_db.fetchall()
for i in cursor:
    studentID = i[0]
    name = i[1]
    level = i[2]
    print(studentID, name, level)
con_db.close()
print(" Success ")


# print(sql1)
