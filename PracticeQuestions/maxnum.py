# Find the max
items = {
    1: 2,
    2: 10,
    3: 6,
    4: 15,
    5: 23
}
max_num = 0
result = []
for num in items:
    if items.get(num) > max_num:
        max_num = items.get(num)
    result.append(items.get(num))

print("Maximum Number is: ", max_num)
result.sort()
print(result)
result.reverse()
print(result)
# print(result.reverse())
