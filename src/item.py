class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def on_take(self):
        print(f'You picked up the {self.name}')

    def on_drop(self):
        print(f'You dropped a {self.name}')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print('You dropped your lightsource. That was stupid.')
