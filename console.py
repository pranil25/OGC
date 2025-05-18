products = {
    "Fruits": {
        101: {"name": "Apple", "price": 160, "stock": 50},
        102: {"name": "Banana", "price": 20, "stock": 100},
        103: {"name": "Orange", "price": 50, "stock": 80},
        104: {"name": "Grapes", "price": 90, "stock": 60}
    },
    "Vegetables": {
        201: {"name": "Potato", "price": 25, "stock": 150},
        202: {"name": "Onion", "price": 30, "stock": 120},
        203: {"name": "Tomato", "price": 28, "stock": 90},
        204: {"name": "Spinach", "price": 15, "stock": 40}
    },
    "Salt & Spices": {
        301: {"name": "Salt", "price": 60, "stock": 200},
        302: {"name": "Turmeric Powder", "price": 55, "stock": 70},
        303: {"name": "Chilli Powder", "price": 70, "stock": 65},
        304: {"name": "Coriander Powder", "price": 65, "stock": 80}
    },
    "Tea Supplies": {
        401: {"name": "Tea", "price": 120, "stock": 50},
        402: {"name": "Sugar", "price": 45, "stock": 100},
        403: {"name": "Milk", "price": 30, "stock": 80},
        404: {"name": "Coffee", "price": 150, "stock": 40}
    },
    "Grains & Pulses": {
        501: {"name": "Rice", "price": 50, "stock": 200},
        502: {"name": "Wheat", "price": 42, "stock": 150},
        503: {"name": "Toor Dal", "price": 90, "stock": 90},
        504: {"name": "Moong Dal", "price": 85, "stock": 85}
    }
}
def view_products():
    print("All Products")
    for categories,items in products.items():    ##calling dictionary
        print(f"categories:")
        for id,data in items.items():
            print(f"{id}.{data['name']}-{data['price']}per unit")

cart={}
def find_product(id):
    for category_items in products.values():
        if id in category_items:
            return category_items[id]
    return None
def add_to_cart():
    try:
        view_products()  # Show products
        id_input = input("Enter Product ID to add to cart: ").strip()

    
        if not id_input.isdigit():
            print(" Please enter a valid numeric Product ID.")
            return
        id = int(id_input)

        product = find_product(id)
        if not product:
            print(" Invalid Product ID. Please try again.")
            return

        qty_input = input(f"Enter quantity for {product['name']}: ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print(" Quantity must be a positive number.")
            return
        qty = int(qty_input)

        if id in cart:
            cart[id] += qty
        else:
            cart[id] = qty

        print(f" {product['name']} (x{qty}) added to cart.")

    except Exception as e:
        print(f" An unexpected error occurred: {e}")
def view_cart():
   total=0

   for id, quantity in cart.items():
    product = find_product(id)
    if product is None:
        print(f"Product ID {id} not found!")
        continue
    name = product['name']
    price = product['price']
    subtotal = price * quantity
    total += subtotal
    print(f"{name} - {quantity} x ₹{price} = ₹{subtotal}")

def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return
    view_cart()
    try:
        id = int(input("Enter ID to remove from cart: "))
        if id in cart:
            del cart[id]
            print("Item removed from cart.")
        else:
            print("Item not found in cart.")
    except ValueError:
        print("Invalid Input")
def checkout():
    if not cart:
        print("Cart is empty.")
        return
    view_cart()
    confirm = input("Do you want to checkout? (yes/n): ").lower()
    if confirm == 'yes':
        print("Order placed successfully! Thank you for shopping.")
        cart.clear()
    else:
        print("Checkout cancelled.")

def main_menu():
    while True:
        print("\n==== Grocery Ordering System ====")
        print("1. View Product Catalog")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Checkout")
        print("6. Exit")
        print("(Choose a number between 1 and 6)")

        try:
            user_input = input("Enter your choice: ")
            
            choice = int(user_input)

            match choice:
                case 1:
                    view_products()
                case 2:
                    add_to_cart()
                case 3:
                    view_cart()
                case 4:
                    remove_from_cart()
                case 5:
                    checkout()
                case 6:
                    print("Thank you for shopping with us!")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 6.")

        except EOFError:
            print("Input failed (EOFError). Check your terminal environment.")
            break  

        except ValueError:
            print("Invalid input. Please enter a valid number.")



if __name__ == "__main__":
    main_menu()



        
