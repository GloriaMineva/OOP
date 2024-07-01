class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        """adds the product in the storage if there is enough space for it"""
        if self.capacity > 0:
            Storage.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return Storage.storage


user_capacity = 4
storage = Storage(user_capacity)
for i in range(6):
    user_product = input()
    storage.add_product(user_product)
print(storage.get_products())




