import re

products = [
    "Apple iPhone 15",
    "Apple iPhone 15 Pro",
    "Samsung Galaxy S24",
    "Samsung Galaxy A55",
    "OnePlus Nord CE 4",
    "OnePlus 12",
    "HP Pavilion Laptop",
    "Dell Inspiron Laptop",
    "Apple MacBook Air",
    "Sony Wireless Headphones"
]


def search_products(keyword, search_type):
    matches = []

    for product in products:

        if search_type == "exact":
            pattern = r"\b" + re.escape(keyword) + r"\b"

        elif search_type == "prefix":
            pattern = r"\b" + re.escape(keyword)

        elif search_type == "suffix":
            pattern = re.escape(keyword) + r"\b"

        elif search_type == "partial":
            pattern = re.escape(keyword)

        else:
            print("Invalid search type")
            return []

        if re.search(pattern, product, re.IGNORECASE):
            matches.append(product)

    return matches


# Example searches

keyword = "apple"
search_type = "partial"

results = search_products(keyword, search_type)

print("Search Keyword :", keyword)
print("Search Type    :", search_type)
print("\nMatching Products:")

for product in results:
    print("-", product)

print("\nTotal Matching Products:", len(results))