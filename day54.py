import csv
with open("day54Totals.csv") as f:
    reader = csv.DictReader(f)
    total = 0
    for row in reader:
        price = float(row["Cost"]) * float(row["Quantity"])
        total += price 
    print(round(total,2))