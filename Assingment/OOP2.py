class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, num_items):
        total_price = 0
        if num_items <= 9:
            total_price = num_items * self.price
        elif 10 <= num_items <= 99:
            total_price = (num_items - 1) * self.price
            total_price += self.price * 0.9
        elif num_items > 99:
            total_price = (num_items - 1) * self.price
            total_price += self.price * 0.8

        return total_price

    def make_purchase(self, num_items):
        if num_items > self.amount:
            return f"Not enough in stock: have {self.amount} ea. Need {num_items} ea."
        self.amount -= num_items
        total_price = self.get_price(num_items)
        return f"Total price for {num_items} items: {total_price:.2f}"

order = [
    Product("Pencil", 1200, 1000),
    Product("Lotion", 5000, 8000),
    Product("Liptic", 120, 200),
    Product("Cusion", 150, 180),
    Product("Powder", 380, 500)
]

for product in order:
    print(f"\nProduct: {product.name}")
    print(f"Price for 5 items (No Discount): {product.get_price(5):.2f}")
    print(f"Price for 10 items (10% Discount on 1 item): {product.get_price(10):.2f}")
    print(f"Price for 20 items (10% Discount on 1 item): {product.get_price(20):.2f}")
    print(f"Price for 100 items (20% Discount on 1 item): {product.get_price(100):.2f}")
    print(product.make_purchase(20))
