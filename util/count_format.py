"""Script to count the number of resources and products in the registry YAML file."""

import yaml
from collections import Counter

with open("registry/kgs.yml") as f:
    data = yaml.safe_load(f)

format_counter = Counter()
resource_category_counter = Counter()
product_category_counter = Counter()
total_resources = 0
total_products = 0

for resource in data.get("resources", []):
    total_resources += 1
    category = resource.get("category", "Unknown")
    resource_category_counter[category] += 1

    for product in resource.get("products", []):
        total_products += 1
        product_category = product.get("category", "Unknown")
        product_category_counter[product_category] += 1

        fmt = product.get("format")
        if fmt:
            format_counter[fmt] += 1

print("Resource counts by category:")
for category, count in resource_category_counter.most_common():
    print(f"{category}: {count}")
print(f"Total resources: {total_resources}\n")

print("Product counts by category:")
for category, count in product_category_counter.most_common():
    print(f"{category}: {count}")
print(f"Total products: {total_products}\n")

print("Format counts:")
for fmt, count in format_counter.most_common():
    print(f"{fmt}: {count}")
print(f"Total formats: {sum(format_counter.values())}")
