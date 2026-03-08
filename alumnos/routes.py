from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Alumnos
import forms

# Definimos el Blueprint
alumnos = Blueprint('alumnos', __name__)

@alumnos.route("/", methods=['GET','POST'])  
@alumnos.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("alumnos/index.html", form=create_form, alumno=alumno)

@alumnos.route('/Alumnos', methods=['GET', 'POST'])
def registrar_alumnos():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST': 
        apellidos_juntos = f"{create_form.apaterno.data} {create_form.amaterno.data}"
        
        alum = Alumnos (
            nombre=create_form.nombre.data,
            apellidos=apellidos_juntos,
            email=create_form.correo.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
       
        return redirect(url_for('alumnos.index')) 
    return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET', 'POST'])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        alumn1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        return render_template('alumnos/detalles.html', alumno=alumn1)
    
    
@alumnos.route('/modificar', methods=['GET', 'POST'])
def modificar(): 
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alumn1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alumn1.id
        create_form.nombre.data = alumn1.nombre
        create_form.apaterno.data = alumn1.apellidos 
        create_form.correo.data = alumn1.email 
        create_form.telefono.data = alumn1.telefono
        
    if request.method == 'POST': 
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apaterno.data 
        alum.email = create_form.correo.data
        alum.telefono  = create_form.telefono.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
        
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route('/eliminar', methods=['GET', 'POST'])
def eliminar(): 
    create_form = forms.UserForm2(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum:
            create_form.id.data = id
            create_form.nombre.data = alum.nombre
            create_form.apaterno.data = alum.apellidos
            create_form.correo.data = alum.email
            create_form.telefono.data= alum.telefono
        
    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        if alum:
            db.session.delete(alum)
            db.session.commit()
        return redirect(url_for('alumnos.index'))
        
    return render_template("alumnos/eliminar.html", form=create_form)

