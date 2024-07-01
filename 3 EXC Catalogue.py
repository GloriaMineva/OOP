class Catalogue:


    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        """adds the product to the products' list"""
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        """returns a list containing only the products that start with the given letter"""
        filtered_products = []
        for product in self.products:
            if product[0] == first_letter.upper():
                filtered_products.append(product)
        return filtered_products

    def __repr__(self):
        self.products.sort()
        return f'Items in the {self.name} catalogue:\n' + "\n".join(Catalogue.products)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

