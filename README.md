# Proiect_Rezervari
Proiect de curs la TMPPP

# Setup
1. Cream virtual environement
```
python -m venv{path-ul catre mapa pentru virtual env}
```

2. Deschidem venv
```
virtual\Script\activate
```

3. Instalam dependentele 
```
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
```
 $env:FLSK_APP=".\lab2.py" 
```

5. Deschidem serverul
```
flask run
```

# Design Patterns

## Singleton 
Am adaugat pattern-ul Singleton in methoda Creational denumind clasa DatabaseSession:
```
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
```

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
