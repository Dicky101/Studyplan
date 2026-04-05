semester = ["fall","winter", "spring", "summer"]

class Course:
    def __init__(self, name, course_code, credits=3, offer_semester=None):
        self.name = name
        self.course_code = course_code
        self.credits = credits
        self.offer_semester = offer_semester


    def get_details(self):
        return f"Course: {self.name}, Code: {self.course_code}, Credits: {self.credits}, Offered in: {self.offer_semester}"


if __name__ == "__main__":
    course = Course("Python Basics", "comp1021", 3, "Fall")
    print(course.get_details())