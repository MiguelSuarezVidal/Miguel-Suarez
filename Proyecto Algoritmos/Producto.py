# [
#   {
#     "id": 3,
#     "name": "Filtro de transmisión automática 3",
#     "description": "Producto resistente",
#     "price": 65.98,
#     "category": "grasas",
#     "inventory": 493,
#     "compatible_vehicles": ["Nissan Sentra"]
#   }
#
class Producto:
    def __init__(self, id, name, description, price, category, inventory, compatible_vehicles=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.inventory = inventory
        self.compatible_vehicles = compatible_vehicles
        
    def show(self):
        print(f'''
    
    id: {self.id}
    Name: {self.name}
    Description: {self.description}
    Price: {self.price} 
    Category: {self.category}
    Inventory: {self.inventory}
    Compatible_vehicles: {self.compatible_vehicles}
    ''')
         
    def show_pago(self):
        print(f'''
    ID: {self.id}
    Nombre: {self.name}
    Precio: {self.price}
    Category: {self.category}
    ----------------------------- 
    ''')
                        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "inventory": self.inventory,
            "compatible_vehicles": self.compatible_vehicles
        }