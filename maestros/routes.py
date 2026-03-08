import forms
from . import maestros
from flask import render_template, request, redirect, url_for
from models import db
from models import Maestros 

@maestros.route("/maestros", methods=['GET', 'POST'])
def lista_maestros():
    create_form = forms.UserForm2(request.form)
    lista_m = Maestros.query.all()
    return render_template("maestros/listadoMest.html", form=create_form,
                           maestros=lista_m
    )
    
    
@maestros.route('/maestros/agregar', methods=['GET', 'POST'])
def agregar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        apellidos_juntos = f"{create_form.apaterno.data} {create_form.amaterno.data}"
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=apellidos_juntos,
            email=create_form.correo.data,
            especialidad=create_form.especialidad.data 
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    return render_template("maestros/agregar.html", form=create_form)

@maestros.route("/maestros/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    maest1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    return render_template('maestros/detalleMaes.html', 
                           id=id, 
                           nombre=maest1.nombre, 
                           apellidos=maest1.apellidos, 
                           email=maest1.email)

@maestros.route("/maestros/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        create_form.id.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apaterno.data = maes1.apellidos 
        create_form.correo.data = maes1.email
        create_form.especialidad.data = maes1.especialidad
        
    if request.method == 'POST':
        id = create_form.id.data
        maes = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        maes.nombre = create_form.nombre.data
        maes.apellidos = create_form.apaterno.data
        maes.email = create_form.correo.data
        maes.especialidad = create_form.especialidad.data
        
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    return render_template('maestros/modificarMaes.html', form=create_form)

@maestros.route('/maestros/eliminar', methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    maes = Maestros.query.get(id) 
    
    delete_form = forms.UserForm2(request.form)

    if request.method == 'GET':
        delete_form.id.data = maes.matricula
        delete_form.nombre.data = maes.nombre
        delete_form.apaterno.data = maes.apellidos 
        delete_form.correo.data = maes.email
        delete_form.especialidad.data = maes.especialidad

    if request.method == 'POST':
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))

    return render_template("maestros/eliminar.html", form=delete_form)