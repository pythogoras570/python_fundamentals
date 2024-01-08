class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        avg_grade = sum(self.grades) / len(self.grades)
        return float(f"{avg_grade:.2f}")

    def __repr__(self):
        avg_grade = self.get_average_grade()
        students = ', '.join(self.students)
        return f"The students in {self.name}: {students}. Average grade: {avg_grade}"
