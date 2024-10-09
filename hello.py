def mergeProducts(A, B):
    product_map = {}

    for product in A:
        product_map[product] = True

    for product in B:
        if product in product_map:
            product_map[product] = False
        else:
            product_map[product] = True

    return product_map

A = ["Banana", "Banana", "Apple"]
B = ["Orange", "Apple", "Banana", "Watermelon"]

merged_products = mergeProducts(A, B)
print("Ket qua sau khi nhap san pham tu kho B vao kho A:")
for product, imported in merged_products.items():
    print(f"{product} -> {imported}")
