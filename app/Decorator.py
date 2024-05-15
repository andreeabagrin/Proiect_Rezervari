from abc import ABC, abstractmethod

# Clasa de bază pentru decorarea sălii
class BanquetHallDecorator(ABC):
    @abstractmethod
    def decorate(self):
        pass

# Implementare concretă a sălii de banchete
class BasicBanquetHall:
    def decorate(self):
        print("")

# Decorator pentru tematica de zi de naștere
class BirthdayThemeDecorator(BanquetHallDecorator):
    def __init__(self, banquet_hall):
        self.banquet_hall = banquet_hall

    def decorate(self):
        self.banquet_hall.decorate()
        print("Sala de banchete este decorată în stil zi de nastere.")
        print("Adăugare baloane colorate și decorațiuni specifice pentru ziua de naștere.")

# Decorator pentru tematica Romantic
class RomanticThemeDecorator(BanquetHallDecorator):
    def __init__(self, banquet_hall):
        self.banquet_hall = banquet_hall

    def decorate(self):
        self.banquet_hall.decorate()
        print("Sala de banchete este decorată în stil romantic.")
        print("Adăugare lumânări, petale de trandafiri și alte decorații romantice.")

# Decorator pentru tematica Jazz
class JazzThemeDecorator(BanquetHallDecorator):
    def __init__(self, banquet_hall):
        self.banquet_hall = banquet_hall

    def decorate(self):
        self.banquet_hall.decorate()
        print("Sala de banchete este decorată în stil jazz.")
        print("Adăugare instrumente muzicale, plăci de jazz și alte decorații în stil jazz.")

# Decorator pentru tematica Rock
class RockThemeDecorator(BanquetHallDecorator):
    def __init__(self, banquet_hall):
        self.banquet_hall = banquet_hall

    def decorate(self):
        self.banquet_hall.decorate()
        print("Sala de banchete este decorată în stil rock.")
        print("Adăugare chitare electrice, postere cu trupe rock și alte decorații în stil rock.")

# Decorator pentru tematica Elegant
class ElegantThemeDecorator(BanquetHallDecorator):
    def __init__(self, banquet_hall):
        self.banquet_hall = banquet_hall

    def decorate(self):
        self.banquet_hall.decorate()
        print("Sala de banchete este decorată în stil elegant.")
        print("Adăugare aranjamente florale elegante, draperii de mătase și alte decorații elegante.")

# Utilizare
basic_banquet_hall = BasicBanquetHall()

# Adăugare tematici la decorarea sălii
decorated_birthday_hall = BirthdayThemeDecorator(basic_banquet_hall)
decorated_birthday_hall.decorate()

decorated_romantic_hall = RomanticThemeDecorator(basic_banquet_hall)
decorated_romantic_hall.decorate()

decorated_jazz_hall = JazzThemeDecorator(basic_banquet_hall)
decorated_jazz_hall.decorate()

decorated_rock_hall = RockThemeDecorator(basic_banquet_hall)
decorated_rock_hall.decorate()

decorated_elegant_hall = ElegantThemeDecorator(basic_banquet_hall)
decorated_elegant_hall.decorate()
