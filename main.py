from item import Item
from phone import Phone

# This has overwritten the name attribute of the item1 object
# What if we want to prevent this from happening?
# Like we only have one chance to set the name of the object
# Otherwise, we get error when we try to set the name again
# This is called encapsulation

# print(item1.read_only_name)
# item1.read_only_name = "Phone 3" # AttributeError: can't set attribute 'read_only_name'

# property decorator is used to make the attribute read only

item1 = Phone("Phone", 50, 1)

item1.send_email()
item1.apply_increment(0.2)
print(item1.price)
item1.apply_discount()
print(item1.price)
# item1._Item__connect("Hello")
# Item.__connect("Hello")
