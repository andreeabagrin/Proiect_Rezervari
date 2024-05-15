from flask_sqlalchemy import SQLAlchemy

class DatabaseSession:
    _instance = None

    def __new__(cls, app):
        if cls._instance is None:
            cls._instance = SQLAlchemy(app)
        return cls._instance

class FormBuilder:
    @staticmethod
    def create_form(form_type):
        if form_type == 'login':
            return LoginForm()
        elif form_type == 'register':
            return RegistrationForm()
        elif form_type == 'add_user':
            return AdduserForm()
        elif form_type == 'add_team':
            return AddteamForm()
        elif form_type == 'delete_team':
            return DeleteteamForm()
        elif form_type == 'delete_user':
            return DeleteuserForm()
        elif form_type == 'book_meeting':
            return BookmeetingForm()
        elif form_type == 'cancel_booking':
            return CancelbookingForm()
        elif form_type == 'room_available':
            return RoomavailableForm()
        elif form_type == 'room_occupation':
            return RoomoccupationForm()
        elif form_type == 'meeting_participants':
            return MeetingparticipantsForm()
        elif form_type == 'cost_accrued':
            return CostaccruedForm()
        else:
            raise ValueError("Invalid form type")

