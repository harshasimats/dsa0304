import re

# Sample resume data
resume = """
Name: Rahul Kumar
Email: rahul.kumar@gmail.com
Mobile: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

# 1. Extract candidate name
name = re.search(r"Name:\s*([A-Za-z ]+)", resume)

# 2. Extract email address
email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# 3. Extract mobile number
mobile = re.search(r"\b[6-9]\d{9}\b", resume)

# 4. Detect technical skills
skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills_list:
    if re.search(r"\b" + re.escape(skill) + r"\b", resume, re.IGNORECASE):
        found_skills.append(skill)

# 5. Extract years of experience
experience = re.search(r"Experience:\s*(\d+)\s*years?", resume)

years = int(experience.group(1)) if experience else 0

# 6. Generate structured summary
print("----- Candidate Profile -----")
print("Name       :", name.group(1).strip() if name else "Not Found")
print("Email      :", email.group() if email else "Not Found")
print("Mobile     :", mobile.group() if mobile else "Not Found")
print("Skills     :", ", ".join(found_skills))
print("Experience :", years, "years")

# 7. Check eligibility
if years >= 2 and "Python" in found_skills:
    print("Eligibility: ELIGIBLE")
else:
    print("Eligibility: NOT ELIGIBLE")