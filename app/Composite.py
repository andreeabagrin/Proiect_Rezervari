from abc import ABC, abstractmethod

# Componenta de bază a meniului
class MenuItem(ABC):
    @abstractmethod
    def display(self):
        pass

# Clasa frunză a meniului, reprezentând elemente individuale
class SingleMenuItem(MenuItem):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print(f"{self.name}: {self.description}")

# Clasa compozită a meniului, reprezentând meniuri care conțin mai multe elemente individuale sau alte meniuri
class CompositeMenuItem(MenuItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def remove(self, item):
        self.children.remove(item)

    def display(self):
        print(f"== {self.name} ==")
        for child in self.children:
            child.display()
        print("================")

# Crearea meniurilor
basic_menu = CompositeMenuItem("Meniu de bază")
basic_menu.add(SingleMenuItem("Aperitiv", "Bruschete"))
basic_menu.add(SingleMenuItem("Fel principal", "Pui la grătar"))
basic_menu.add(SingleMenuItem("Desert", "Tiramisu"))

deluxe_menu = CompositeMenuItem("Meniu deluxe")
deluxe_menu.add(SingleMenuItem("Aperitiv", "Caviar"))
deluxe_menu.add(SingleMenuItem("Fel principal", "File mignon"))
deluxe_menu.add(SingleMenuItem("Desert", "Profiterolă"))

vegetarian_menu = CompositeMenuItem("Meniu vegetarian")
vegetarian_menu.add(SingleMenuItem("Aperitiv", "Salată verde"))
vegetarian_menu.add(SingleMenuItem("Fel principal", "Tofu cu legume la grătar"))
vegetarian_menu.add(SingleMenuItem("Desert", "Fructe proaspete"))

bar_menu = CompositeMenuItem("Meniu pentru bar")
bar_menu.add(SingleMenuItem("Băutură", "Cocktail Mojito"))
bar_menu.add(SingleMenuItem("Băutură", "Vin roșu sec"))
bar_menu.add(SingleMenuItem("Băutură", "Apă minerală"))

fourchette_menu = CompositeMenuItem("Meniu fourchette")
fourchette_menu.add(SingleMenuItem("Aperitiv", "Mini-sandwich-uri"))
fourchette_menu.add(SingleMenuItem("Aperitiv", "Rulouri cu somon fumător"))

# Afisarea meniurilor
basic_menu.display()
deluxe_menu.display()
vegetarian_menu.display()
bar_menu.display()
fourchette_menu.display()
