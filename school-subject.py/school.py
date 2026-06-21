student_profile = ("Aarav", "Grade 6", "Section A", 6)
student_name = student_profile[0]
print("First 2 details:",student_profile[0:2])
monday_subjects = {"Math", "Science", "English", "computer", "art"}
tuesday_subjects = {"Math", "Science", "English", "History", "Sports"}
monday_subjects.add("library")
monday_subjects.discard("art")    
all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
print("All subjects:", all_subjects)
print("Common subjects:", common_subjects)
print("Subjects on Monday but not on Tuesday:", monday_subjects.difference(tuesday_subjects))
print("Subjects on Tuesday but not on Monday:", tuesday_subjects.difference(monday_subjects))
subject_teachers = {
    "Math": "Mr. Smith",
    "Science": "Ms. Johnson",
    "English": "Mrs. Lee",
    "History": "Mr. Brown",
    "Sports": "Coach Davis"
}
print("Teacher for Math:", subject_teachers["Math"])
subject_teachers["Computer"] = "Ms. Wilson"
print("Updated subject teachers:", subject_teachers)
print("\nMonday subjects:", monday_subjects)
print("Tuesday subjects:", tuesday_subjects)
print("\nSubject teachers:", subject_teachers)
print("\nStudent Profile:", student_profile)
print("Student Name:", student_name)
print("Student Grade:", student_profile[1])
print("Student Section:", student_profile[2])
print("Student Age:", student_profile[3])
print("\nAfter adding Library to monday:", monday_subjects)
print("After discarding Art from monday:", monday_subjects)
