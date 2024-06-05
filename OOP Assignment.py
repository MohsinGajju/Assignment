class Faculty:
    def _init_(self, name, designation, department):
        self.name = name
        self.designation = designation
        self.department = department
        self.courses_taught = []

    def add_course(self, course):
        self.courses_taught.append(course)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Department: {self.department}")

    def display_courses_taught(self):
        if self.courses_taught:
            print(f"{self.name} teaches the following courses:")
            for course in self.courses_taught:
                print(course)
        else:
            print(f"{self.name} is not assigned to teach any courses yet.")


# Example usage
faculty1 = Faculty("Mr.Zafer", "Professor", "Computer Science")
faculty1.add_course("Introduction to Programming")
faculty1.add_course("Data Structures and Algorithms")

faculty2 = Faculty("Mr.Shahid", "Assistant Professor", "Electrical Engineering")
faculty2.add_course("Circuit Analysis")
faculty2.add_course("Digital Signal Processing")

faculty1.display_info()
faculty1.display_courses_taught()
print("---------------------")
faculty2.display_info()
faculty2.display_courses_taught()
