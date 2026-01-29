# Write your solution here

items = int(input('How many items: '))
items_list = [0] * items

for x in range(0, items):
    items_list[x] = int(input('How many items: '))

print(items_list)
