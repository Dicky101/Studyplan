class Myclass:
    def __init__(self, sem, year,course):
        self.sem = sem
        self.year = year
        self.course = course

    def display(self):
        print(f"Semester: {self.sem}, Year: {self.year}, Course: {self.course}")