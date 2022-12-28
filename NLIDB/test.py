from nltk.tokenize import sent_tokenize, word_tokenize
from corpuss import store, tables, dept, values
from Apps.entry import cur_db, con_db

from Apps import entry

text = "I need the payment list of students in English"
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
tabless = ''
column_name = ''
value = ''

# Extract table names
t1, t2, t3 = "health", "payment", "student"

if t1 in nlq:
    tabless = tables[t1]
elif t2 in nlq:
    tabless = tables[t2]
else:
    tabless = tables[t3]


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
    if tabless == "students":
        sql1 = "select student_id, name, course, level  from " + tabless + " where " + column_name + " = " + value
    elif tabless == "payments":
        sql1 = "SELECT name, course, amount_paid, purpose FROM " + tabless + " p, students s where p.student_id = s.student_id and p." + column_name + " = " + value
    else:
        sql1 = "select student_id from " + tabless + " where " + column_name + " = " + value
else:
    sql1 = "select * from " + tabless

print(sql1)