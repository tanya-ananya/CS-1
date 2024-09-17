'''
This program will keep track of the composition of a container ship and its cargo.

Author: Taaruni Ananya
'''

class Container:
    size = ['1 TEU', '2 TEU']

    cargo_type = {
        'Frozen Food' : 'FF', 
        'Consumer Goods' : 'CG',
        'Processed Goods' : 'PG',
        'Raw Materials' : 'RM',
        'Industrial Equipment' : 'IE'
    }

    def __init__(self, size, cargo):
        self.size = size
        self.cargo = cargo

    def get_size(self):
        return self.size
    
    def get_cargo_type(self):
        return self.cargo

class Container_Ship:
    def __init__(self, max_capacity, max_speed, min_draft, max_draft):
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.min_draft = min_draft
        self.max_draft = max_draft
        containers = []

    container = Container(size, cargo)
    def get_cargo(self):
        cargos = Container.get_size / 20
        return cargos
    
    def get_draft(self):
        draft = (self.max_draft - self.min_draft) * self.max_capacity
        return draft
    
    def get_speed(self):
        min_speed = self.max_speed / 2
        speed = self.max_speed - min_speed
        return speed

    def print_ship(self):
        cargo = Container_Ship.get_cargo()
        draft = Container_Ship.get_draft()
        speed = Container_Ship.get_speed()

        print(f'Cargo: {cargo} TEUs')
        print(f'Draft: {draft} meters')
        print(f'Speed: {speed} knots')
        



