import func_api
import csv
from datetime import date
from pick import pick

items = func_api.receipt.items
today = date.today()
title = 'Where is this receipt from?  '
store = ["Roche Bros", "Trader Joe's"]
store, index = pick(store, title)

def categorize(items):
    with open('input.csv', 'w') as infile:
        writer = csv.writer(infile)
        for item in items:
            title = f'What category is {item.item_name}? '
            category = ["Vegetables", "Grains", "Fruit", "Snacks", "Dairy", "Meat", "Drinks", "Frozen", "Canned Goods", "Other" ]
            category, index = pick(category, title)
            writer.writerow([today, store, item.item_name, item.unit_price, item.unit, category])

