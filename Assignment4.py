# Assignment 4 – Inventory File System
# Build a program that reads employee attendance data from a text/CSV file (each line containing employee name,
#  date and status: Present/Absent) and analyzes attendance patterns, producing a full report.
# Requirements:
# •	Read attendance records from a file attendance.csv using the csv module or manual line parsing.
# •	Calculate the total number of present and absent days for each employee.
# •	Identify and report any employee whose attendance percentage is below 75%.
# •	Write a summary report back out to a new file (attendance_report.txt) using the with statement in write mode.
# •	Provide a way to append a new day's attendance data to the source file without overwriting existing records.
# •	Handle missing files or malformed lines gracefully using appropriate checks.


import csv
import os
if not os.path.exists("employee_data.csv"):
    with open("employee_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee_name", "Date", "Status"])
        writer.writerow(["Karthika N", "17/10/2026", "present"])
        writer.writerow(["Nida", "17/10/2026", "Absent"])
        writer.writerow(["Prarthana", "17/10/2026", "present"])
        writer.writerow(["Karthika N", "18/10/2026", "present"])
        writer.writerow(["Nida", "18/10/2026", "Absent"])
        writer.writerow(["Prarthana", "18/10/2026", "present"])

print("CSV created")

employee = {}

with open("employee_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        status = row[2].lower()

        if name not in employee:
            employee[name] = [0, 0]

        if status == "present":
            employee[name][0] += 1
        elif status == "absent":
            employee[name][1] += 1

with open("attendance_report.txt", "w") as file:
    for key, value in employee.items():
        present = value[0]
        absent = value[1]
        total = present + absent

        percentage = (present / total) * 100

        file.write("Name: " + key + "\n")
        file.write("Present: " + str(present) + "\n")
        file.write("Absent: " + str(absent) + "\n")
        file.write("Percentage: " + str(percentage) + "%\n")

        if percentage < 75:
            file.write("Low attendance\n")

        file.write("\n")

print("Report saved successfully")
with open("attendance_report.txt",'r')as file:
    print(file.read())

choice = input("Do you want to add new attendance? (yes/no): ").lower()
if choice=="yes":
    Employee_name = input("Enter employee name: ").strip()
    Date = input("Enter date (DD/MM/YYYY): ").strip()
    Status = input("Enter status (Present/Absent): ").strip().capitalize()

    if Employee_name and Date and Status in ["Present", "Absent"]:
        with open("employee_data.csv", 'a', newline="") as file:
            writer=csv.writer(file)
            writer.writerow([Employee_name,Date,Status])
        print("New attendance record appended successfully.")
        print("Run the program again to update the report.")
    else:
        print("Invalid input. Please enter valid details.")
    
