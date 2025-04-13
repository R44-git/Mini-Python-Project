menu = {
    'Pizza': 40,
    'Burger': 30,
    'Pasta': 50,
    'Salad': 20,
    'coffee': 80,
}

print("Welcome to the restaurant!")
print("Here is the menu:")
print("Pizza -  Rs. 40\nBurger - Rs. 30\nPasta - Rs. 50\nSalad - Rs. 20\ncoffee - Rs. 80")

order_total = 0
item_1 = input("Please enter the name of item you want to order : ")
 
if item_1 in menu:
    order_total += menu[item_1] 
    print(f"your item {item_1} has been added to your order")

else:
    print("Sorry, we don't have that item on the menu.")  

another_item = input("Do you want to order another item? (yes/no): ").lower()    
if another_item == "yes":
    item_2 = input("Please enter the name of item you want to order : ")
    
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"your item {item_2} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu.")

print(f"Your total order amount is Rs. {order_total}")         

