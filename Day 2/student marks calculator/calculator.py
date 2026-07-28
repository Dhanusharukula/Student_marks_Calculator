#Student Marks Calculator
name = input("Enter Student name ")

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))

total = subject1 + subject2 + subject3
average = total / 3
percentage = (total/300) * 100

print("Student Name: ", name)
print("Total Marks: ", total)
print("Average Marks: ", average)
print("Percentage: ", percentage, "%")

if percentage >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")


