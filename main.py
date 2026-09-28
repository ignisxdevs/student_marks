# Module 10: Modules & Packages (Importing our helper file)
import helper

# Module 1 & 2: Variables and Strings
welcome_text = "WELCOME TO B.TECH STUDENT RECORD SYSTEM"
print("=" * 45)
print(welcome_text)
print("=" * 45)

# Module 7: Core Data Structures (A standard Python List to hold subjects)
subjects = ["Maths", "Physics", "Python Programming", "Basic Electrical"]

# Module 8: Control Flow (While loop)
while True:
    print("\nMenu:")
    print("1. Enter Student Details & Marks")
    print("2. Exit Program")

    # Module 4: Input / Output
    user_choice = input("Enter your choice (1 or 2): ")

    if user_choice == "1":
        # Module 4: Input & Module 6: Type Conversion (string to int)
        roll = int(input("\nEnter Roll Number: "))
        student_name = input("Enter Student Name: ")

        # Module 12: Creating an object from class
        student1 = helper.Student(roll, student_name)

        print(f"\nEnter marks out of 100 for {len(subjects)} subjects:")
        total = 0

        # Module 8: For Loop (iterating through the list)
        for sub in subjects:
            # Module 6: Converting string input to int
            mark = int(input("Enter marks for " + sub + ": "))
            student1.add_mark(mark)
            total = total + mark  # Module 3: Arithmetic addition

        # Display results
        print("\n" + "-" * 30)
        print("       REPORT CARD")
        print("-" * 30)
        student1.show_info()

        # Display marks from array (Module 11)
        print("Marks stored in Array:", student1.marks_array.tolist())
        print("Total Marks Obtained:", total, "out of", len(subjects) * 100)

        # Calling function from helper module (Module 9 & 10)
        percent, grade = helper.calculate_grade(total, len(subjects))
        print("Percentage:", round(percent, 2), "%")
        print("Final Grade:", grade)

        # Module 13 call
        helper.predict_next_semester(percent)
        print("-" * 30)

    elif user_choice == "2":
        print("\nThank you for using the system. Goodbye!")
        break  # Module 8: break statement

    else:
        print("Invalid choice! Please choose 1 or 2.")