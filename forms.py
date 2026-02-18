from wtforms import Form
from wtforms import IntegerField,StringField,PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm2(Form):
    matricula=IntegerField("id")

    nombre=StringField("Nombre",[
         validators.DataRequired(message="El campo es requerido"),
         validators.length(min=4, max=10, message="Ingrese nombre valido")
    ])
    apaterno=StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese apellido valido")

    ])
    email=EmailField("Email", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])

 