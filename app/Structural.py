class Observer:
    def update(self, event_data):
        pass

class Observable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, event_data):
        for observer in self._observers:
            observer.update(event_data)

class EmailSender(Observer):
    def update(self, event_data):
        # Implement logic to send an email
        user_email = event_data['email']
        message = "Thank you for registering!"
        # Example email sending code (replace with your email sending logic)
        send_email(user_email, "Registration Confirmation", message)