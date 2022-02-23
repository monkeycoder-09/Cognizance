stu_details = [
    ["Rollno.", "Name", "Marks"],
    [1, "Abc", 90],
    [2, "Def", 95],
    [3, "Ghi", 85]
]

#To print out entire list in Tabular form
for row in stu_details:
    print(*row)

#To print Second row only
""" second_row = (stu_details[2])
print(*second_row) """