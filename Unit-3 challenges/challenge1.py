def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices
  
# List of products
products = ['apple', 'banana', 'apple', 'cherry', 'apple', 'orange']

# Target product to search for
target_product = 'apple'

# Perform linear search
result = linear_search_product(products, target_product)

# Print the result
if result:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found.")
