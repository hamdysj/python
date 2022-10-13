# Write a Python script to multiply all items in a dictionary
multiply_items = {
    1: 2,
    2: 3,
    3: 3
}
result = 1

for num in multiply_items:
    result = result * multiply_items.get(num)
print(result)
