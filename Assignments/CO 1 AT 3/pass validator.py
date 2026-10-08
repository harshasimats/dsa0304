import re


def validate_email(email):
    """
    Validates email according to the given rules:
    - Starts with an alphabet
    - Can contain letters, digits, '.', '_'
    - Domain contains only alphabets
    - Extension: com, org, edu, net, in
    """

    pattern = r"^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$"

    return bool(re.fullmatch(pattern, email))


def validate_password(password):
    """
    Password rules:
    - Minimum 8 characters
    - At least one uppercase
    - At least one lowercase
    - At least one digit
    - At least one special character
    """

    pattern = (
        r"^(?=.*[A-Z])"
        r"(?=.*[a-z])"
        r"(?=.*\d)"
        r"(?=.*[@#$%&!])"
        r".{8,}$"
    )

    return bool(re.fullmatch(pattern, password))


def validate_mobile(mobile):
    """
    Mobile number rules:
    - Exactly 10 digits
    - First digit must be 6-9
    """

    pattern = r"^[6-9]\d{9}$"

    return bool(re.fullmatch(pattern, mobile))


def validate_user(email, password, mobile):

    print("\n----- Validation Result -----")

    # Email validation
    if validate_email(email):
        print("Email           : Valid Email")
    else:
        print("Email           : Invalid Email")

    # Password validation
    if validate_password(password):
        print("Password        : Strong Password")
    else:
        print("Password        : Weak Password")

    # Mobile validation
    if validate_mobile(mobile):
        print("Mobile Number   : Valid Mobile Number")
    else:
        print("Mobile Number   : Invalid Mobile Number")


# -------------------------------
# Test Case 1 - Valid Input
# -------------------------------

email = "rahul123@gmail.com"
password = "Rahul@123"
mobile = "9876543210"

print("TEST CASE 1")
print("Email:", email)
print("Password:", password)
print("Mobile:", mobile)

validate_user(email, password, mobile)


# -------------------------------
# Test Case 2 - Invalid Input
# -------------------------------

email = "123rahul@gmail.com"
password = "rahul123"
mobile = "1234567890"

print("\nTEST CASE 2")
print("Email:", email)
print("Password:", password)
print("Mobile:", mobile)

validate_user(email, password, mobile)