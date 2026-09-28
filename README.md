# B.Tech Student Record System

## 1. Project Overview

The **B.Tech Student Record System** is a simple, menu-driven Python
program that accepts a student's roll number, name, and marks in four
subjects. It calculates the total marks, percentage, and final grade,
then displays a report card and a simple next-semester performance
forecast.

The project is divided into two Python files: `main.py` handles the
menu, input, and report card, while `helper.py` contains the `Student`
class and the functions used for grade calculation and forecasting.

## 2. Features

-   Enter a student's roll number and name.
-   Enter marks out of 100 for Maths, Physics, Python Programming, and
    Basic Electrical.
-   Store the entered marks in a Python integer array during program
    execution.
-   Display the student's details and marks in a report-card format.
-   Calculate and display total marks and percentage.
-   Assign a grade based on the percentage:
    -   90% and above: A+
    -   75% to below 90%: A
    -   60% to below 75%: B
    -   40% to below 60%: C
    -   Below 40%: Fail
-   Display a simple next-semester performance forecast based on the
    percentage.
-   Provide a menu option to enter another student's details or exit the
    program.

## 3. Technologies and Tools Used

-   **Programming Language:** Python 3
-   **Python concepts:** variables, strings, input/output, type
    conversion, operators, lists, loops, conditional statements,
    functions, modules, arrays, and object-oriented programming
-   **Files:** `main.py` and `helper.py`
-   **IDE/Editor:** Python IDLE or Visual Studio Code

No external Python packages are required.

## 4. Steps to Install and Run the Project

1.  Make sure Python 3 is installed on your computer.

2.  Keep `main.py` and `helper.py` in the same folder.

3.  Open a terminal or command prompt in that folder.

4.  Run the following command:

    ``` bash
    python main.py
    ```

5.  Choose **1** to enter student details and marks, or **2** to exit.

6.  Follow the prompts to enter the roll number, name, and marks for all
    four subjects.

If your system uses the `python3` command, run `python3 main.py`
instead.

## 5. Instructions for Testing

1.  Run `main.py`.
2.  Select option **1** from the menu.
3.  Enter a roll number and student name.
4.  Enter marks for all four subjects when prompted.
5.  Check that the report card displays the entered details, marks,
    total, percentage, and grade.
6.  Test different marks to check the grade categories (A+, A, B, C, and
    Fail).
7.  Check the forecast message for percentages both below and at/above
    75%.
8.  Select option **1** again to enter another set of details, or option
    **2** to exit.
9.  Enter an invalid menu choice and check that the program displays its
    invalid-choice message.

**Note:** The current program displays the entered student's report
during the running session. It does not save records to a CSV file or
database, so the details are not retained after the program closes.
