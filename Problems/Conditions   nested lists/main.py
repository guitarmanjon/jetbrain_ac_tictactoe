# the list "students" is already defined
# students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]
top_students = [student[0] for student in students if student[1] == "A"]
#
# top_students = []
# for student in students:
#     if student[1] == "A":
#         top_students.append(student[0])
print(top_students)
