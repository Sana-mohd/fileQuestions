#item no. quantity,price, total amount of price
import csv
f=open("ITEM.csv","r")
csv_reader = csv.reader(f)
next(csv_reader)
sum=0
for i in csv_reader:
    sum+=int(i[-1])
print("Total Price",sum)
