from student import Student
from patient import Patient

John_Long = Student()
John_Long.first_name = "John"
John_Long.last_name = "Long"
John_Long.cohort = 36
John_Long.age = 46
# print(John_Long.age)
# print(John_Long.full_name)
print(John_Long)

pat1 = Patient("493-70-0000", "10/28/73", "7000111222", "John", "Long", "301 Plus Park Blvd")

pat1.address = "1638 County Rd 642"
print(pat1)
print(pat1.ssn, pat1.dob)
print(pat1.full_name)







