from course import Course
from getcatolog import get_info_from_website, extract_math_courses_from_pdf_url
from Myclass import Myclass

#input from user
# year=input("Enter the year of admission: ")
# school=input("Enter the school: ")
# major=input("Enter the semester: ")
# max_credits=int(input("Enter the maximum credits you can take: "))


#get course codes
course_code_list=get_info_from_website("https://prog-crs.hkust.edu.hk/ugcourse", r'[A-Z]{4}')
print("Course codes:", course_code_list)

#get the course list of the major
year = "2024-25"
major_list = get_info_from_website("https://prog-crs.hkust.edu.hk/ugprog/" + year,  r'[A-Z]{2,6}',r'[A-Z]+-[A-Z]+')
print("Major list:", major_list)
