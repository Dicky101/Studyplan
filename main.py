from course import Course
from getcatolog import get_subject_codes, extract_math_courses_from_pdf_url
from Myclass import Myclass

#input from user
# year=input("Enter the year of admission: ")
# school=input("Enter the school: ")
# major=input("Enter the semester: ")
# max_credits=int(input("Enter the maximum credits you can take: "))

#get the course list of the major
course_code=get_subject_codes()

print("Course codes:", course_code)
