product_type_list = ["Television", "Computer"]
product_sub_type_list = ["Laptop", "All-in-One", "Smart TV"]
base_product = {
        "Name": "",
        "Sku": "",
        "Upc": "",
        "Brand": "",
        "Type": "",
        "SubType": []
    }
ext_television = {
    "Screen Size": "",
    "Model": "",
    "Smart": "",
    "Wifi": "",
    "Ethernet": "",
    "Hdmi Ports": "",
    "USB Ports": "",
    "Refresh Rate": "",
    "Auxiliary": "",
    "Optical": "",
    "Coaxial Audio": "",
    "Component": "",
    "Composite": "",
}

def product_types():
    return

class Product:
    def __init__(self, load=None):

        if not load:
            self.container = base_product
        else:
            self.container = load

    @property
    def name(self):
        return self.container["Name"]

    @property
    def sku(self):
        return self.container["Sku"]

    @property
    def upc(self):
        return self.container["Upc"]

    @property
    def type(self):
        return self.container["Type"]

class Television(Product):

    def __init__(self, load=None):

        if not load:
            self.container = {**base_product, **ext_television}
        else:
            self.container = load

    @property
    def screen_size(self):
       return self.container["Screen Size"]

    def model(self):
        return self.container["Model"]


def create_new_product():
    pass
    # product = Product(base_product)

Television()


