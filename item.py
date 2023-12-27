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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all_items.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        
    @property
    # Property decorator is used to make the attribute read only
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
        
    def calculate_total(self):
        return self.__price * self.quantity
        
    # in order to instantiate the object from the csv file, we  need to create a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items:
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    def __connect(self, smth):
        print("Establishing a connection to another object...")
        return smth
    def __prepare_body(self):
        return    print("Preparing the body of the email...")
    
    def __send(self):
        print("Sending the email...")
        
    def send_email(self):
        self.__connect(self.__prepare_body())
        self.__send()
    
    
