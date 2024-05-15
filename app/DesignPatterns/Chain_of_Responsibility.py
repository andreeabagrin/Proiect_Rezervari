class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor is not None:
            self._successor.handle_request(request)


class AvailabilityCheckHandler(Handler):
    def handle_request(self, request):
        if request == "Verificare disponibilitate sala":
            print("Sala este disponibilă pentru rezervare.")
        else:
            super().handle_request(request)


class ReservationDetailsHandler(Handler):
    def handle_request(self, request):
        if request == "Obținere detalii rezervare":
            print("Detaliile rezervării sunt...")
        else:
            super().handle_request(request)


class ConfirmationHandler(Handler):
    def handle_request(self, request):
        if request == "Confirmare rezervare":
            print("Rezervarea a fost confirmată.")
        else:
            super().handle_request(request)


# Utilizare
availability_handler = AvailabilityCheckHandler()
reservation_details_handler = ReservationDetailsHandler(availability_handler)
confirmation_handler = ConfirmationHandler(reservation_details_handler)

confirmation_handler.handle_request("Verificare disponibilitate sala")
confirmation_handler.handle_request("Obținere detalii rezervare")
confirmation_handler.handle_request("Confirmare rezervare")
