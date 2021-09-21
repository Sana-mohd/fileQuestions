import pickle
dict={}
f=open("example.bin","ab")
total_number=int(input("enter the No.of students: "))
for i in range(total_number):
    print("Enter details of the student",i+1)
    dict["Roll No."]=int(input("enter the roll number: "))
    dict["Name"]=input("enter the Name of the student: ")
pickle.dump(dict,f)

