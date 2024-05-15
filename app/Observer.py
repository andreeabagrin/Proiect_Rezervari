from abc import ABC, abstractmethod

class Client_Observer():
    observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass

class EmailObserver(Observer):
    def update(self, *args, **kwargs):
        if "user_registered" in kwargs:
            self.send_email(kwargs["user_registered"])

    def send_email(self, user):
        # Your email sending logic here
        print(f"Email sent to {user.username} at {user.email}")