import re

text = "My email is student@example.com and my phone number is 9876543210."

# 1. Search for an email address
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.search(email_pattern, text)

if email:
    print("Email found:", email.group())
else:
    print("Email not found")

# 2. Search for a 10-digit phone number
phone_pattern = r'\b\d{10}\b'
phone = re.search(phone_pattern, text)

if phone:
    print("Phone number found:", phone.group())
else:
    print("Phone number not found")

# 3. Find all numbers in the text
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)

# 4. Match a word at the beginning of a string
word = "Python is easy to learn."
if re.match(r'Python', word):
    print("The text starts with Python")
else:
    print("The text does not start with Python")