import  datetime

now = datetime.datetime.now()

print("Student: Kenneth Del Poso Salloman")
print("Student ID: 231-0690")
print(f"Date/Time: {now} ")

issue = input("Describe Network Problem: ")

file = open("./network_issue.txt","a")
file.write(issue + "\n")
file.close()
