class FoodItem:
    def __init__(self,item_id,name,price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def display_info(self):
        print("---------------------")
        print(f"| {self.item_id:<2}| {self.name:<10}|{self.price:<3}|")

class Order:
    def __init__(self):
        self.cart = []

    def add_item(self,food_item,quantity):
        self.cart.append([food_item.item_id,food_item,quantity])

    def remove_item(self):
        f_id = int(input("enter item id:"))
        for item in self.cart:
            fid,food,quantity = item
            if fid == f_id:
                self.cart.remove(item)
                break
            else:
                print("No,Item Found In This id")

    def calculate_total(self):
        return sum(food.price * quantity for _,food,quantity in self.cart)

    def display_order(self):
        if not self.cart:
            print("Cart is empty.")
            return

        print("--------------------Your Cart-------------")
        print("| id  | name       | price | qty | total |")
        print("------------------------------------------")
        for fid, food, quantity in self.cart:
            total = food.price * quantity
            print(f"| {fid:<3} | {food.name:<10} | {food.price:<5} | {quantity:<3} | {total:<5} |")
        print("------------------------------------------")
        print("Total amount: ", self.calculate_total())


menu_list = [
    FoodItem(1, "Pizza", 150),
    FoodItem(2, "Burger", 100),
    FoodItem(3, "Sandwich", 80),
    FoodItem(4, "Fries", 60),
    FoodItem(5, "Coke", 40)
]
o = Order()

while True:
    print("---------Food-Menu----------")
    print("1.Show Food Menu")
    print("2.Add Item To Cart")
    print("3.Remove Item From Cart")
    print("4.View Cart")
    print("5.Checkout")

    choice = int(input("\nenter choice:"))

    if choice == 1:
        print("---Food-Menu---")
        for i in menu_list:
            i.display_info()

    elif choice == 2:
        fid = int(input("enter food id: "))
        quantity = int(input("enter quantity: "))

        for i in menu_list:
            if i.item_id == fid:
                o.add_item(i, quantity)
                print("Food Item added to cart")
                break
        else:
            print("Invalid food id")

    elif choice == 3:
        o.remove_item()

    elif choice == 4:
        o.display_order()

    elif choice == 5:
        print("Total bill:",o.calculate_total())
        break
    else:
        print("Invalid Choice")
