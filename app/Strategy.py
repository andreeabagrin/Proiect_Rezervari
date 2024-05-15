class PricingStrategy:
    def calculate_price(self, hall, reservation_details):
        pass


class HourlyRateStrategy(PricingStrategy):
    def calculate_price(self, hall, reservation_details):
        if hall == 1:
            return reservation_details * 230
        elif hall == 2:
            return reservation_details * 540
        elif hall in (3, 4):
            return reservation_details * 970
        else:
            # Handle unknown hall numbers
            return 0  # Or raise an exception, depending on your requirements



class PerPersonRateStrategy(PricingStrategy):
    def calculate_price(self, hall, reservation_details):
        if hall == 1:
            return reservation_details * 30
        elif hall == 2:
            return reservation_details * 50
        elif hall in (3, 4):
            return reservation_details * 70
        else:
            # Handle unknown hall numbers
            return 0  # Or raise an exception, depending on your requirements


class FixedRateStrategy(PricingStrategy):
    def calculate_price(self, hall, reservation_details):
        if hall == 1:
            return 500
        elif hall == 2:
            return 1000
        elif hall in (3, 4):
            return 1500
        else:
            # Handle unknown hall numbers
            return 0  # Or raise an exception, depending on your requirements



