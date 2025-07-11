products = {}
while True:
    print("\nProduct Menu:")
    print("1. Add new product")
    print("2. Update price of a product")
    print("3. Find products within a price range")
    print("4. Display all products")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter product name: ")
        if name in products:
            print("Product already exists.")
        else:
            price = float(input("Enter product price: "))
            products[name] = price
            print("Product added.")

    elif choice == "2":
        name = input("Enter product name to update: ")
        if name in products:
            price = float(input("Enter new price: "))
            products[name] = price
            print("Price updated.")
        else:
            print("Product not found.")
    elif choice == "3":
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        print(f"Products between {min_price} and {max_price}:")
        found = False
        for name, price in products.items():
            if min_price <= price <= max_price:
                print(f"{name}: {price}")
                found = True
        if not found:
            print("No products found in this range.")

    elif choice == "4":
        print("All Products:")
        for name, price in products.items():
            print(f"{name}: {price}")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1-5.")