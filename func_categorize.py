import func_api
import csv

items = func_api.receipt.items

with open('input.csv', 'w') as infile:
    writer = csv.writer(infile)
    for item in items:
        category = input(f'What category is {item.item_name}? ')
        writer.writerow([item.item_name, item.unit_price, item.unit, category])

