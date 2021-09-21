#voter id,voter name ,voter age,return whose age is greater than 65
import csv
f=open("VOTER.csv","r")
csv_reader = csv.reader(f)
next(csv_reader)
print("Voter_Id",",","VoterName",",","VoterAge ")
for row in csv_reader:
    if int(row[-1])>65:
        print(', '.join(row))