from langchain_core.tools import tool

@tool
def attendance_calculator(total_classes: int, attended_classes: int) -> str:
    """
    Calculate attendance percentage and determine exam eligibility.

    Inputs:
    - total_classes: Total conducted classes
    - attended_classes: Classes attended by student

    Returns:
    - Attendance percentage
    - Eligibility status based on 75% attendance rule
    """
    percentage = (attended_classes / total_classes) * 100

    if percentage >= 75:
        status = "Eligible for Exam"
    else:
        status = "Not Eligible for Exam"

    return f"Attendance Percentage: {percentage:.2f}%\nStatus: {status}"


@tool
def result_calculator(m1: int, m2: int, m3: int, m4: int, m5: int) -> str:
    """
Calculate total marks, percentage and academic grade.

Inputs:
- marks obtained in subjects

Returns:
- Total marks
- Percentage
- Grade
"""

    average = (m1 + m2 + m3 + m4 + m5) / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    status = "Pass" if average >= 50 else "Fail"

    return (
        f"Average Marks: {average:.2f}\n"
        f"Grade: {grade}\n"
        f"Status: {status}"
    )


@tool
def fee_balance_calculator(total_fee: float, amount_paid: float) -> str:
    """Calculate pending fee amount And  
    Calculate total hostel fee.

    IMPORTANT:
    Convert years into months.

    Example:
    1 year = 12 months
    2 years = 24 months

    Inputs:
    monthly_fee
    months_stayed
    """
    pending = total_fee - amount_paid
    return f"Pending Fee Amount: ₹{pending}"


@tool
def library_fine_calculator(delayed_days: int) -> str:
    """
Calculate library fine based on overdue days.

Inputs:
- Number of overdue days

Returns:
- Fine amount
"""
    fine = delayed_days * 5
    return f"Library Fine Amount: ₹{fine}"


@tool
def hostel_fee_calculator(monthly_fee: float, months_stayed: int) -> str:
    """
Calculate hostel fee and pending balance.

Inputs:
- Hostel fee amount
- Amount paid

Returns:
- Remaining hostel fee balance
"""
    total = monthly_fee * months_stayed
    return f"Total Hostel Fee: ₹{total}"


@tool
def student_information(student_id: str) -> str:
    """Retrieve student details using Student ID"""

    students = {
        "101": {
            "name": "Sai Kiran",
            "branch": "CSE",
            "year": "2nd Year"
        },
        "102": {
            "name": "Rahul",
            "branch": "ECE",
            "year": "2nd Year"
        }
    }

    if student_id in students:
        student = students[student_id]

        return (
            f"Student ID: {student_id}\n"
            f"Name: {student['name']}\n"
            f"Branch: {student['branch']}\n"
            f"Year: {student['year']}"
        )

    return "Student not found"