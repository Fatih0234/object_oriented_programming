class Item:
    
    # Class Attributes
    pay_rate = 0.8 # 20% discount on all items
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
item1 = Item("Phone", 50, 1)
item2 = Item("Laptop", 1000, 2)
item1.name = "Phone 2"

item2.has_numpad = False

print(Item.__dict__) # All the attributed of the class
print(item1.__dict__) # All the attributed of the object
# as in the case of object, it first looks for the attribute in the object and then in the class

print(item1.calculate_total())

# if we have different discount rate for laptops
item2.pay_rate = 0.7
print(item2.pay_rate)
print(item2.calculate_total())
print(item2.price)
item2.apply_discount()
print(item2.price)
