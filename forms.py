from wtforms import Form
from wtforms import IntegerField, StringField, EmailField
from wtforms import validators

class UserForm2(Form):
    id = IntegerField("id") 

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese nombre valido")
    ])
    apaterno = StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField("Amaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Email", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])
    
    telefono = StringField("Telefono", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    especialidad = StringField("Especialidad", [
        validators.DataRequired(message="El campo es requerido ")
    ])