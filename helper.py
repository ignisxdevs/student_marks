# Module 11: Array data structure (stores integers)
import array

# Module 12: Object Oriented Programming (A simple class)
class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        # Module 11: 'i' means this array stores whole numbers (integers)
        self.marks_array = array.array('i', [])

    def add_mark(self, score):
        self.marks_array.append(score)

    def show_info(self):
        print("Roll Number:", self.roll_number)
        print("Student Name:", self.name)


# Module 9: Functions in Python
def calculate_grade(total_marks, subject_count):
    # Module 3: Operators (/ and *)
    # Module 5: Precedence & Associativity (Parentheses ( ) run first, then division)
    max_marks = subject_count * 100
    percentage = (total_marks / max_marks) * 100

    # Module 8 logic inside a function
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return percentage, grade


# Module 13: Look into the Future (Simple forecast for upcoming semesters)
def predict_next_semester(current_percentage):
    print("\n--- Future Performance Forecast ---")
    if current_percentage >= 75:
        print("Forecast: High chance of clearing campus placements on first attempt!")
    else:
        print("Forecast: Work harder in Semester 2 to reach a distinction score (75%+).")