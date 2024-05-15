# Proiect_Rezervari
Proiect de curs la TMPPP

# Setup
1. Cream virtual environement
```bash
python -m venv{path-ul catre mapa pentru virtual env}
```

2. Deschidem venv
```bash
virtual\Script\activate
```

3. Instalam dependentele 
```bash
 pip install flask
 pip install Flask python-dateutil 
 pip install flask-sqlalcheamy mysqlclient  
 pip install flask-bcrypt
 pip install flask 
 pip install flask-wtf 
 pip install flask-sqlalchemy  
 pip install flask-migrate
 pip install flask-login 
 pip install Werkzeug==2.2.2  
```

4. Instalam environement variables
```bash
 $env:FLSK_APP=".\lab2.py" 
```

5. Deschidem serverul
```bash
flask run
```

# Design Patterns

## Singleton 
Am adaugat pattern-ul Singleton in methoda Creational denumind clasa DatabaseSession:
```python
class DatabaseSession:
    _instance = None

    def __new__(cls, app):
        if cls._instance is None:
            cls._instance = SQLAlchemy(app)
        return cls._instance
```
putem observa ca se instantiaza obiectul o singura data la creare iar mai departe utilizam doar obiectul creat pentru executarea querry-urilor sau orice altceva.

## Factory
Metoda factory e bazata pe crearea formelor in front si citirea dadtelor din acestea. In dependenta de endpoint-ul la care a venit requestul, se creaza un obiect de o anumita forma:
```python

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    fullname = StringField('Full Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    teamId = IntegerField('Team number', validators=[DataRequired()])
    teamName = StringField('Team name', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:  # username exist
            raise ValidationError('Please use a different username.')

    def validate_teamId(self, teamId):
        team = Team.query.filter_by(id=teamId.data).first()
        if team is not None:
            if team.teamName != self.teamName.data:
                raise ValidationError('Team name does not match, try again.')


class AdduserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    fullname = StringField('Full Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    teamId = IntegerField('Team number', validators=[DataRequired()])
    teamName = StringField('Team name', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:  # username exist
            raise ValidationError('Please use a different username.')

    def validate_teamId(self, teamId):
        team = Team.query.filter_by(id=teamId.data).first()
        if team is not None:
            if team.teamName != self.teamName.data:
                raise ValidationError('Team name does not match, try again.')

class FormFactory:
    @staticmethod
    def create_form(form_type):
        if form_type == 'login':
            return LoginForm()
        elif form_type == 'register':
            return RegistrationForm()
        elif form_type == 'add_user':
            return AdduserForm()
        # Add more form types as needed
        else:
            raise ValueError("Invalid form type")
```

## Builder
Codul reprezintă un formular de rezervare a întâlnirilor într-o aplicație Flask, folosind pattern-ul de programare "builder". Clasa BookmeetingForm definește câmpurile și logica de validare a formularului, în timp ce metoda BookmeetingFormBuilder permite construirea pas cu pas a formularului, setând diferitele sale atribute. Astfel, se promovează o construcție flexibilă a obiectului formular, cu gestionarea logică a validării datelor.

```python
class BookMeetingFormBuilder:
    def __init__(self):
        self.form = BookmeetingForm()

    def set_title(self, title):
        self.form.title.data = title
        return self

    def set_rooms(self, rooms):
        self.form.rooms.data = rooms
        return self

    #...soo one ...

    def build(self):
        return self.form
```

## Composite
Codul implementează pattern-ul de proiectare "composite", care permite crearea și gestionarea unei structuri ierarhice de elemente meniului. Clasa de bază MenuItem definește interfața comună pentru toate elementele de meniu, iar clasele SingleMenuItem și CompositeMenuItem reprezintă elementele individuale și compuse ale meniului, respectiv. Astfel, se oferă posibilitatea de a trata uniform atât elementele individuale, cât și compuse ale meniului.

```python
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
```

## Decorator
Codul utilizează pattern-ul "Decorator" pentru a adăuga funcționalități suplimentare sau decorări la o clasă de bază, în acest caz `BasicBanquetHall`. Fiecare decorator (`BirthdayThemeDecorator`, `RomanticThemeDecorator`, etc.) primește o instanță a sălii de banchete și îi adaugă decorările specifice tematicii, extinzând funcționalitatea inițială a sălii. Astfel, se oferă flexibilitate în modificarea și extinderea comportamentului sălii de banchete în funcție de nevoile și preferințele utilizatorului.

```python
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

```

## Proxy
Codul demonstrează utilizarea pattern-ului "Proxy" pentru a controla accesul și a adăuga funcționalități suplimentare în jurul obiectului real al sălii de banchete. Clasa `BanquetHallProxy` acționează ca un intermediar între client și obiectul real al sălii de banchete, efectuând verificări înainte și după rezervare prin suprascrierea metodei `reserve()`. Astfel, se asigură un acces controlat și se adaugă logica suplimentară fără a modifica direct obiectul real.

```python
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
```

## Observer
Codul implementează pattern-ul "Observer" pentru a permite notificarea automată a unor obiecte observatoare atunci când un obiect observabil suferă o modificare. Clasa Observable gestionează lista de obiecte observatoare și include metode pentru atașarea, detasarea și notificarea acestora. Clasa EmailSender exemplifică un obiect observator care reacționează la notificările obținute, în acest caz trimițând un email de confirmare.

```python
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
```

## Strategy
Codul implementează pattern-ul "Strategy", oferind mai multe strategii de calcul a prețului pentru rezervările sălii de banchete. Fiecare strategie (Orar, Pe Persoană, Fix) este reprezentată printr-o clasă separată care extinde clasa de bază PricingStrategy și implementează metoda calculate_price(). Aceasta permite flexibilitate în selectarea și schimbarea strategiilor de calcul a prețului în funcție de cerințele specifice ale aplicației.

```python
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
```

## Command
În codul dat, pattern-ul "Command" este implicit utilizat în gestionarea formularelor Flask. Clasele de formular (LoginForm, RegistrationForm, etc.) acționează ca și comenzi, reprezentând acțiuni posibile ale utilizatorului. Clasa FormFactory acționează ca un creator, furnizând instanțe de formular în funcție de tipul specificat, în timp ce clasa BookMeetingFormBuilder poate fi văzută ca un comandant, permițând construirea și configurarea dinamică a formularului de rezervare a întâlnirii.



