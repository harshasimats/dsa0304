import re


def validate_registration(reg_no, email, course_code, semester, mobile):

    print("----- University Registration Validation -----")

    valid = True

    # 1. Validate Register Number
    if re.fullmatch(r"\d{2}[A-Z]{3}\d{3}", reg_no):
        print("Register Number : Valid")
    else:
        print("Register Number : Invalid")
        valid = False

    # 2. Validate Institutional Email
    if re.fullmatch(r"[a-zA-Z0-9._%+-]+@university\.edu", email):
        print("Institutional Email : Valid")
    else:
        print("Institutional Email : Invalid")
        valid = False

    # 3. Validate Course Code
    if re.fullmatch(r"[A-Z]{3}\d{3}", course_code):
        print("Course Code : Valid")
    else:
        print("Course Code : Invalid")
        valid = False

    # 4. Validate Semester
    if re.fullmatch(r"[1-8]", semester):
        print("Semester : Valid")
    else:
        print("Semester : Invalid")
        valid = False

    # 5. Validate Mobile Number
    if re.fullmatch(r"[6-9]\d{9}", mobile):
        print("Mobile Number : Valid")
    else:
        print("Mobile Number : Invalid")
        valid = False

    # Final Registration Status
    print("\n----- Final Registration Status -----")

    if valid:
        print("Registration Successful")
    else:
        print("Registration Failed")


# Test Case
validate_registration(
    "23CSE101",
    "rahul@university.edu",
    "CSE101",
    "5",
    "9876543210"
)