#Favorite Season & Price Checker Program
allowed: tuple[str, ...] = ("Autumn", "Summer", "Spring", "Winter")
season = input("Pick season:")

#Season section
if season in allowed:
    print("Your season is set to:", season)
else:
    print("Invalid season. Please choose from Autumn, Summer, Spring, or Winter.")

#Price section
price = (input("What is the price of this item?"))

if price.replace('.', '', 1).isdigit():
    price = float(price)
    print("The price of the item is set to:", price)
else:
    print("Invalid price. Please enter a valid number.")