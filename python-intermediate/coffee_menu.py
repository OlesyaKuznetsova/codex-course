class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, coffee_name):
        return self.menu.get(coffee_name, None)
    
    def add_item(self, coffee_name, price):
        if coffee_name not in self.menu:
            self.menu[coffee_name] = price
    