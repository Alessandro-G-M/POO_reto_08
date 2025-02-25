class Order:
    def __init__(self):
        self.items = []
    
    #* Se agrega el __iter__ para que sea posible iterar sobre ella
    def __iter__(self):
        return OrderIter(self.items)
    

    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

#* Nueva clase iterador para order
class OrderIter:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index +=1
            return item
        else:
            raise StopIteration
    



class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Beverage(MenuItem):    
    def __init__(self, name, price, size: str = 'Normal'):
        if size.upper() == 'GRANDE': 
            price += 1000
        elif size.upper() == 'PEQUEÑO': 
            price -= 1000
        super().__init__(name, price)
        self.size = size.upper()


class MainDish(MenuItem):
    def __init__(self, name: str, price: float, protein_choice: str = 'chicken'):
        if protein_choice.upper() == 'BEEF': 
            price += 3000
        elif protein_choice.upper() == 'SEAFOOD': 
            price += 2500
        super().__init__(name, price)
        self.protein_choice = protein_choice.upper()


class Starters(MenuItem):
    def __init__(self, name: str, price: float, extra_portion: bool = False):
        if extra_portion: 
            price += 2000
        super().__init__(name, price)
        self.extra_portion = extra_portion


class Desserts(MenuItem):
    def __init__(self, name: str, price: float, topping: str = 'none'):
        if topping.upper() == 'CHOCOLATE': 
            price += 500
        elif topping.upper() == 'CARAMEL': 
            price += 1000
        elif topping.upper() == 'NUTS': 
            price += 1200
        super().__init__(name, price)
        self.topping = topping.upper()




#! MAIN

def main():
    # Crear ítems del menú
    beverage1 = Beverage(name="Coca Cola", price=2000, size="Grande")
    beverage2 = Beverage(name="Agua Mineral", price=1500, size="Pequeño")

    main_dish1 = MainDish(name="Pollo Asado", price=10000, protein_choice="chicken")
    main_dish2 = MainDish(name="Filete de Res", price=15000, protein_choice="beef")
    main_dish3 = MainDish(name="Cazuela de Mariscos", price=20000, protein_choice="seafood")

    starter1 = Starters(name="Ensalada César", price=5000, extra_portion=True)
    starter2 = Starters(name="Sopa de Tomate", price=4000, extra_portion=False)

    dessert1 = Desserts(name="Brownie", price=3000, topping="chocolate")
    dessert2 = Desserts(name="Helado", price=3500, topping="caramel")
    dessert3 = Desserts(name="Tarta de Frutas", price=4000, topping="none")



    # Ejemplo Iterable e Iterador

    order = Order()
    order.add_item(beverage1)
    order.add_item(main_dish1)
    order.add_item(dessert1)
    order.add_item(main_dish3)

    for item in order:
        print(f'Item: {item.name}, Precio: {item.price}')
        
if __name__ == '__main__':
    main()



        
        
    
        