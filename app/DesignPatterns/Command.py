class Command:
    def execute(self):
        pass


class ConfirmReservationCommand(Command):
    def __init__(self, reservation):
        self._reservation = reservation

    def execute(self):
        self._reservation.confirm()


class CancelReservationCommand(Command):
    def __init__(self, reservation):
        self._reservation = reservation

    def execute(self):
        self._reservation.cancel()


# Utilizare
class Reservation:
    def confirm(self):
        print("Rezervarea a fost confirmată.")

    def cancel(self):
        print("Rezervarea a fost anulată.")


reservation = Reservation()
confirm_command = ConfirmReservationCommand(reservation)
cancel_command = CancelReservationCommand(reservation)

# Execuție comenzi
confirm_command.execute()
cancel_command.execute()
