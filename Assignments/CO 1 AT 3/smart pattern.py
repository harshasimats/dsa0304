import re


# ------------------------------------------------
# Search Functions
# ------------------------------------------------

def search_date(text):
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(pattern, text)


def search_phone(text):
    pattern = r"\b[6-9]\d{9}\b"
    return re.findall(pattern, text)


def search_hashtag(text):
    pattern = r"#[A-Za-z0-9_]+"
    return re.findall(pattern, text)


def search_mention(text):
    pattern = r"@[A-Za-z0-9_]+"
    return re.findall(pattern, text)


def search_word(text, word):
    pattern = r"\b" + re.escape(word) + r"\b"
    return re.findall(pattern, text, re.IGNORECASE)


def search_prefix(text, prefix):
    words = re.findall(r"\b[A-Za-z]+\b", text)

    return [
        word for word in words
        if word.lower().startswith(prefix.lower())
    ]


def search_suffix(text, suffix):
    words = re.findall(r"\b[A-Za-z]+\b", text)

    return [
        word for word in words
        if word.lower().endswith(suffix.lower())
    ]


# ------------------------------------------------
# Display Results
# ------------------------------------------------

def display_results(title, results):

    print("\n" + title)

    if results:
        for item in results:
            print("-", item)
        print("Total Matches:", len(results))
    else:
        print("No matching pattern found.")


# ------------------------------------------------
# Main Program
# ------------------------------------------------

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

print("==========================================")
print(" SMART REGEX PATTERN MATCHING ENGINE")
print("==========================================")

print("\nInput Text:")
print(text)

while True:

    print("\n----------- MENU -----------")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        results = search_date(text)
        display_results("Date Search Results", results)

    elif choice == "2":

        results = search_phone(text)
        display_results("Phone Number Search Results", results)

    elif choice == "3":

        results = search_hashtag(text)
        display_results("Hashtag Search Results", results)

    elif choice == "4":

        results = search_mention(text)
        display_results("Mention Search Results", results)

    elif choice == "5":

        prefix = input("Enter prefix: ")

        results = search_prefix(text, prefix)
        display_results("Prefix Search Results", results)

    elif choice == "6":

        suffix = input("Enter suffix: ")

        results = search_suffix(text, suffix)
        display_results("Suffix Search Results", results)

    elif choice == "7":

        word = input("Enter word: ")

        results = search_word(text, word)
        display_results("Word Search Results", results)

    elif choice == "8":

        print("Exiting program...")
        break

    else:

        print("Invalid choice. Please select 1-8.")