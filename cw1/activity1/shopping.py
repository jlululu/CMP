# -*- coding: utf-8 -*-
import json
import time

class Product:
    def __init__(self, name, price, quantity, EAN_identifier, brand):
        self.type = 'Product'
        self.name = name
        self.price = price
        self.quantity = quantity
        self.EAN_identifier = EAN_identifier
        self.brand = brand
        
    def to_json(self):
        summary = {"type":self.type, "name":self.name, "price":self.price, "quantity":self.quantity, "EAN_identifier":self.EAN_identifier, "brand":self.brand}
        return json.dumps(summary)


class Clothing(Product):
    def __init__(self, name, price, quantity, EAN_identifier, brand, size, material):
        super().__init__(name, price, quantity, EAN_identifier, brand)
        self.type = 'Clothing'
        self.size = size
        self.material = material
        
    def to_json(self):
        summary = {"type":self.type, "name":self.name, "price":self.price, "quantity":self.quantity, "EAN_identifier":self.EAN_identifier, "brand":self.brand, "size":self.size, "material": self.material}
        return json.dumps(summary, indent = 2)
    
        
class Food(Product):
    def __init__(self, name, price, quantity, EAN_identifier, brand, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, EAN_identifier, brand)
        self.type = 'Food'
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans
        
    def to_json(self):
        summary = {"type":self.type, "name":self.name, "price":self.price, "quantity":self.quantity, "EAN_identifier":self.EAN_identifier, "brand":self.brand, "expiry_date":self.expiry_date, "gluten_free": self.gluten_free, "suitable_for_vegans":self.suitable_for_vegans}
        return json.dumps(summary, indent = 2)
    

class Smartphone(Product):
    def __init__(self, name, price, quantity, EAN_identifier, brand, operating_system, memory_storage_capacity, display_size, color):
        super().__init__(name, price, quantity, EAN_identifier, brand)   
        self.type = 'Smartphone'
        self.operating_system = operating_system
        self.memory_storage_capacity = memory_storage_capacity
        self.display_size = display_size
        self.color = color
        
    def to_json(self):
        summary = {"type":self.type, "name":self.name, "price":self.price, "quantity":self.quantity, "EAN_identifier":self.EAN_identifier, "brand":self.brand, "operating_system":self.operating_system, "memory_storage_capacity":self.memory_storage_capacity, "display_size":self.display_size, "color":self.color}
        return json.dumps(summary, indent = 2)
    


class ShoppingCart:
    #initialize the cart and the number of products in the cart
    def __init__(self):
        self.cart = dict()
        self.num = 0
    
    def addProduct(self,p):
        '''1.the product has been added before
           2.firstly added'''
        k = (p.price,p.EAN_identifier)
        if k in self.cart.keys():
            self.cart.get(k).quantity = self.cart.get(k).quantity + p.quantity
        else:
            self.cart[k] = p
        self.num = self.num + p.quantity
        print("The product {} has been added to the cart.".format(p.name))
        print("The cart contains {} products.".format(self.num))
            
    def removeProduct(self,p):
        k = (p.price,p.EAN_identifier)
        self.cart.pop(k)
        self.num = self.num - p.quantity
        print("{} successfully removed from the cart.".format(p.name))
        print("The cart contains {} products.".format(self.num))
    
    def showSummary(self):
        print("This is the total of the expenses:")
        i = 1
        cost = 0
        for p in self.cart.values():
            if p.quantity == 1:
                print("{} - {} = £{}".format(i,p.name,p.price))
                cost = cost + p.price
            else:
                print("{} - {} * {} = £{}".format(i,p.quantity,p.name,p.quantity*p.price))
                cost = cost + p.quantity * p.price
            i = i + 1
        print("Total = £{}".format(cost))
    
    def changeProductQuantity(self, p, q):
        #when q = 0, basically it means we should remove the product.
        k = (p.price,p.EAN_identifier)
        if q == 0:
            self.cart.pop(k)
            self.num = self.num - p.quantity
        else:
            self.num = self.num + q - self.cart[k].quantity
            self.cart[k].quantity = q
        print("The quantity of {} has been changed to {}.".format(p.name,q))


#do shopping
customer = ShoppingCart()
cart = customer.cart

def A():
    flag = True
    while flag == True:
        print("Adding a new product:")
        type = input("Insert its type: ")
        if type == 'Clothing':
            name = input("Insert its name: ")
            if name == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(name):
                print('Invalid input. Please try again.')
                continue
            #price should be a positive float number
            try:
                price_s = input("Insert its price(£): ")
                if price_s == 'C':
                    print("The current operation is cancelled.")
                    return
                price = float(price_s)
                if price <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            #quantity should be a positive integer
            try:
                quantity_s = input("Insert its quantity: ")
                if quantity_s == 'C':
                    print("The current operation is cancelled.")
                    return
                quantity = int(quantity_s)
                if quantity <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            brand = input("Insert its brand: ")
            if brand == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(brand):
                print('Invalid input. Please try again.')
                continue
            EAN_identifier = input("Insert its EAN code: ")
            if EAN_identifier == 'C':
                print("The current operation is cancelled.")
                return
            #EAN identifier should be a 13-digit number, the combination of EAN code and price should be unique for each kind of products
            if EAN_identifier.isdigit() == False or len(EAN_identifier) != 13:
                print("Invalid input. Please try again.")
                continue
            k = (price,EAN_identifier)
            if k in cart.keys():
                product = cart.get(k)
                if product.type != type or product.name != name or product.brand != brand:
                    print("Invalid input. Please try again.")
                    continue
            size = input("Insert its size: ")
            if size == 'C':
                print("The current operation is cancelled.")
                return
            if not len(size):
                print("Invalid input. Please try again.")
                continue
            material = input("Insert its material: ")
            if material == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(material):
                print("Invalid input. Please try again.")
                continue
            p = Clothing(name, price, quantity, EAN_identifier, brand, size, material)
            customer.addProduct(p)
            #adding successfully, then break the loop
            flag = False
        elif type == 'Food':
            name = input("Insert its name: ")
            if name == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(name):
                print('Invalid input. Please try again.')
                continue
            #price should be a positive float number
            try:
                price_s = input("Insert its price(£): ")
                if price_s == 'C':
                    print("The current operation is cancelled.")
                    return
                price = float(price_s)
                if price <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            #quantity should be a positive integer
            try:
                quantity_s = input("Insert its quantity: ")
                if quantity_s == 'C':
                    print("The current operation is cancelled.")
                    return
                quantity = int(quantity_s)
                if quantity <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            brand = input("Insert its brand: ")
            if brand == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(brand):
                print('Invalid input. Please try again.')
                continue
            EAN_identifier = input("Insert its EAN code: ")
            if EAN_identifier == 'C':
                print("The current operation is cancelled.")
                return
            #EAN identifier should be a 13-digit number, the combination of EAN code and price should be unique for each kind of products
            if EAN_identifier.isdigit() == False or len(EAN_identifier) != 13:
                print("Invalid input. Please try again.")
                continue
            k = (price,EAN_identifier)
            if k in cart.keys():
                product = cart.get(k)
                if product.type != type or product.name != name or product.brand != brand:
                    print("Invalid input. Please try again.")
                    continue
            #expiry date should be in the format:dd/mm/YY and should be later than now
            expiry_date = input("Insert its expiry date(DD/MM/YY): ")
            if expiry_date == 'C':
                print("The current operation is cancelled.")
                return
            try:
                temp = time.strptime(expiry_date,"%d/%m/%Y")
                now = time.localtime()
                if temp < now:
                    print("This item has already expired.")
                    return
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            gluten_free = input("Insert if it's gluten-free(y/n): ")
            if gluten_free == 'C':
                print("The current operation is cancelled.")
                return
            if gluten_free != 'y' and gluten_free != 'n':
                print("Invalid input. Please try again.")
                continue
            suitable_for_vegans = input("Input if it's suitable for vegans(y/n): ")
            if suitable_for_vegans == 'C':
                print("The current operation is cancelled.")
                return
            if suitable_for_vegans != 'y' and suitable_for_vegans != 'n':
                print("Invalid input. Please try again.")
                continue
            p = Food(name, price, quantity, EAN_identifier, brand, expiry_date, gluten_free, suitable_for_vegans)
            customer.addProduct(p)
            #adding successfully, then break the loop
            flag = False
        elif type == 'Smartphone':
            name = input("Insert its name: ")
            if name == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(name):
                print('Invalid input. Please try again.')
                continue
            #price should be a positive float number
            try:
                price_s = input("Insert its price(£): ")
                if price_s == 'C':
                    print("The current operation is cancelled.")
                    return
                price = float(price_s)
                if price <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            #quantity should be a positive integer
            try:
                quantity_s = input("Insert its quantity: ")
                if quantity_s == 'C':
                    print("The current operation is cancelled.")
                    return
                quantity = int(quantity_s)
                if quantity <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            brand = input("Insert its brand: ")
            if brand == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(brand):
                print('Invalid input. Please try again.')
                continue
            EAN_identifier = input("Insert its EAN code: ")
            if EAN_identifier == 'C':
                print("The current operation is cancelled.")
                return
            #EAN identifier should be a 13-digit number, the combination of EAN code and price should be unique for each kind of products
            if EAN_identifier.isdigit() == False or len(EAN_identifier) != 13:
                print("Invalid input. Please try again.")
                continue
            k = (price,EAN_identifier)
            if k in cart.keys():
                product = cart.get(k)
                if product.type != type or product.name != name or product.brand != brand:
                    print("Invalid input. Please try again.")
                    continue
            operating_system = input("Insert its operating system: ")
            if operating_system == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(operating_system):
                print("Invalid input. Please try again.")
                continue
            #memory storage capacity should be a positive integer
            try:
                memory_storage_capacity_s = input("Insert its memory storage capacity(GB): ")
                if memory_storage_capacity_s == 'C':
                    print("The current operation is cancelled.")
                    return
                memory_storage_capacity = int(memory_storage_capacity_s)
                if memory_storage_capacity <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            #display size should be a positive float number
            try:
                display_size_s = input("Insert its display size(Inches): ")
                if display_size_s == 'C':
                    print("The current operation is cancelled.")
                    return
                display_size = float(display_size_s)
                if display_size <= 0:
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
            color = input("Insert its color: ")
            if color == 'C':
                print("The current operation is cancelled.")
                return
            #in case empty input
            if not len(color):
                print("Invalid input. Please try again.")
                continue
            p = Smartphone(name, price, quantity, EAN_identifier, brand, operating_system, memory_storage_capacity, display_size, color)
            customer.addProduct(p)
            #adding successfully, then break the loop
            flag = False
        elif type == 'C':
            print("The current operation is cancelled.")
            flag = False
        else:
            print("Invalid input. Please try again.")
        

def R():
    #in case the cart is empty
    if not customer.num:
        print('The cart is empty.')
        return
    flag = True
    while flag == True:
        EAN_identifier = input("What is the EAN identifier of the product you want to remove? ")
        if EAN_identifier == 'C':
            print("The current operation is cancelled.")
            return
        #EAN identifier should be a 13-digit number
        if EAN_identifier.isdigit() == False or len(EAN_identifier) != 13:
            print("Invalid input. Please try again.")
            continue
        #price should be a positive float number
        price_s = input("What is the price of the product you want to remove? ")
        if price_s == 'C':
            print("The current operation is cancelled.")
            return
        try:
            price = float(price_s)
            if price <= 0:
                print("Invalid input. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        k = (price,EAN_identifier)
        #in case the item is not in the cart
        if k in cart.keys():
            customer.removeProduct(cart.get(k))
            flag = False
        else:
            print("This product is not in the cart.")
            flag = False


def Q():
    #in case the cart is empty
    if not customer.num:
        print('The cart is empty.')
        return
    flag = True
    while flag == True:
        EAN_identifier = input("What is the EAN identifier of the product you want to change? ")
        if EAN_identifier == 'C':
            print("The current operation is cancelled.")
            return
        #EAN identifier should be a 13-digit number
        if EAN_identifier.isdigit() == False or len(EAN_identifier) != 13:
            print("Invalid input. Please try again.")
            continue
        # price should be a positive float number
        price_s = input("What is the price of the product you want to change?")
        if price_s == 'C':
            print("The current operation is cancelled.")
            return
        try:
            price = float(price_s)
            if price <= 0:
                print("Invalid input. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        k = (price,EAN_identifier)
        if k in cart.keys():
            #quantity should be an integer and should not be less than 0
            try:
                q_s = input("Insert the quantity you want: ")
                if q_s == 'C':
                    print("The current operation is cancelled.")
                    return
                q = int(q_s)
                if q < 0:
                    print("Invalid input. Please try again.")
                else:
                    customer.changeProductQuantity(cart.get(k), q)
                    flag = False
            except ValueError:
                print("Invalid input. Please try again.")
        else:
            print("This product is not in the cart.")
            flag = False


def E():
    #In case the cart is empty.
    if customer.num:
        content = []
        for p in cart.values():
            print(p.to_json())
    else:
        print("The cart is empty.")            


def H():
    print("The program supports the following commands:")
    commond = {'[A]':'Add a new product to the cart', '[R]':'Remove a product from the cart', '[S]':'Print a summary of the cart', '[Q]':'Change the quantity of a product', '[E]':'Export a JSON version of the cart', '[C]':'Cancel the current operation', '[T]':'Terminate the program', '[H]':'List the supported commands'}
    for k in commond.keys():
        print("{} - {}".format(k,commond.get(k)))

print('The program has started.')
print('Insert your next command (H for help):')
terminated = False
while not terminated:
    c = input("Type your next command:")
    if c == 'T':
        terminated = True
    elif c == 'A':
        A()
    elif c == 'R':
        R()
    elif c == 'S':
        customer.showSummary()
    elif c == 'Q':
        Q()
    elif c == 'E':
        E()
    elif c == 'C':
        print("The current operation is cancelled.")
    elif c == 'H':
        H()
    else:
        print("Command not recognised. Please try again.")
print('Goodbye.')