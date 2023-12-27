import csv

class Item:
    
    # Class Attributes
    pay_rate = 0.8 # 20% discount on all items
    all_items = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all_items.append(self)
        
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    # in order to instantiate the object from the csv file, we  need to create a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            print(reader)
            items = list(reader)
        
        for item in items:
            print(item)
            cls(name=item.get("name"), price=float(item.get("price")), quantity=int(item.get("quantity")))
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    
        
    def __repr__(self): # => __repr__ is used to represent the object 
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    # def __str__(self):
    #     return f"{self.name} -> {self.calculate_total()}"

# item1 = Item("Phone", 50, 1)
# item2 = Item("Laptop", 1000, 2)
# item3 = Item("Mouse", 10, 4)
# item4 = Item("Keyboard", 20, 3)
# item5 = Item("Monitor", 100, 1)
# item6 = Item("HDMI Cable", 5, 4)
# item7 = Item("Charger", 15, 2)


# print(Item.all_items) # => __repr__ is used to represent the object
# print(item1) # => __str__ is used to represent the object

# I have items.csv file with empyt 
# name,price,quantity
# let's write the items we have now into csv file using csv module

# with open("items.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "price", "quantity"])
#     for item in Item.all_items:
#         writer.writerow([item.name, item.price, item.quantity])


Item.instantiate_from_csv()

print(Item.all_items)
print(Item.is_integer(5.5 ))


        
