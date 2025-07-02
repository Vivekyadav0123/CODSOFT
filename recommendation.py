import csv

# Load product data
products = []
descriptions = []

try:
    with open("C:/Users/vivek yadav/OneDrive/Desktop/products.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row['product'])
            descriptions.append(row['description'].lower())
except FileNotFoundError:
    print("Error: products.csv not found. Please check the file path.")
    exit()

# Recommend similar products
def recommend(product_name):
    lower_products = [p.lower() for p in products]

    if product_name.lower() not in lower_products:
        print(f"\nProduct '{product_name}' not found.")
        return

    index = lower_products.index(product_name.lower())
    reference_words = set(descriptions[index].split())

    print(f"\nSimilar products to '{products[index]}':\n")
    score_list = []

    for i, desc in enumerate(descriptions):
        if i == index:
            continue
        words = set(desc.split())
        match_score = len(reference_words & words)
        score_list.append((i, match_score))

    sorted_scores = sorted(score_list, key=lambda x: x[1], reverse=True)

    found = False
    for i, score in sorted_scores[:5]:
        if score > 0:
            print(f"- {products[i]}  (relevance: {score})")
            found = True

    if not found:
        print("No similar products found.")

# Allow user to try multiple times
print("\nAvailable products:")
for name in products:
    print("-", name)

print("\nType the product name to get recommendations.")
print("Type 'exit' to quit the program.\n")

while True:
    user_input = input("Search product: ")
    if user_input.lower() == "exit":
        print("Thank you for using the recommendation system.")
        break
    recommend(user_input)
    print()  # blank line for better readability
