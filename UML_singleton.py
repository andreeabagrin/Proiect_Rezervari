from subprocess import Popen, PIPE
import os

def generate_class_diagram(code, output_file):
    # Create PlantUML code for class diagram
    plantuml_code = f"""
    @startuml
    {code}
    @enduml
    """

    # Generate class diagram using PlantUML
    p = Popen(['plantuml', '-tpng', '-o', os.path.dirname(output_file), '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(input=plantuml_code.encode())

    if p.returncode == 0:
        with open(output_file, 'wb') as f:
            f.write(out)
        return True
    else:
        print("Error:", err.decode())
        return False

# Example class structure
class_code = r"""
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
"""

# Output file name
output_file = 'class_diagram.png'

# Generate class diagram and save it to a PNG file
success = generate_class_diagram(class_code, output_file)

if success:
    print(f"Class diagram saved to {output_file}")
else:
    print("Failed to generate class diagram")
