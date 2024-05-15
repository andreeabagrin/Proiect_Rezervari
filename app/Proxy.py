from abc import ABC, abstractmethod

# Clasa de bază pentru sala de banchete
class BanquetHall(ABC):
    @abstractmethod
    def reserve(self):
        pass

# Implementare concretă a sălii de banchete
class RealBanquetHall(BanquetHall):
    def reserve(self):
        print("Sala de banchete a fost rezervată.")

# Proxy pentru sala de banchete
class BanquetHallProxy(BanquetHall):
    def __init__(self):
        self.real_hall = RealBanquetHall()

    def reserve(self):
        self.perform_checks_before_reservation()
        self.real_hall.reserve()
        self.perform_checks_after_reservation()

    def perform_checks_before_reservation(self):
        print("Verificări înainte de rezervare: Disponibilitatea sălii, plata avansului, etc.")

    def perform_checks_after_reservation(self):
        print("Verificări după rezervare: Confirmare rezervare, trimitere confirmare către client, etc.")

# Utilizare
banquet_hall_proxy = BanquetHallProxy()
banquet_hall_proxy.reserve()
