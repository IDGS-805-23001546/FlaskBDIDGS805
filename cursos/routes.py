from flask import Blueprint, flash, render_template, request, redirect, url_for
from models import db, Curso, Maestros, Alumnos

cursos = Blueprint('cursos', __name__)

@cursos.route("/cursos")
def index():
    lista_cursos = Curso.query.all()
    return render_template("cursos/index.html", cursos=lista_cursos)

@cursos.route("/cursos/agregar", methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nuevo = Curso(
            nombre=request.form.get('nombre'),
            descripcion=request.form.get('descripcion'),
            maestro_id=request.form.get('maestro_id')
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    
    lista_m = Maestros.query.all()
    return render_template("cursos/agregar.html", maestros=lista_m)

@cursos.route("/cursos/inscribir/<int:id>", methods=['GET', 'POST'])
def inscribir(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        alumno = Alumnos.query.get(alumno_id)
        
        if alumno and alumno not in curso.alumnos:
            curso.alumnos.append(alumno)
            db.session.commit()
            flash('Alumno inscrito exitosamente.', 'success')
            return redirect(url_for('cursos.index'))
        else:
            # Esta es la parte que faltaba para la alerta
            flash('Este alumno ya se encuentra inscrito en este curso.', 'error')
            return redirect(url_for('cursos.inscribir', id=id))
    
    todos_los_alumnos = Alumnos.query.all()
    # Cambié a inscribir.html para que coincida con tu archivo
    return render_template("cursos/inscribir.html", curso=curso, alumnos=todos_los_alumnos)

@cursos.route("/cursos/modificar/<int:id>", methods=['GET', 'POST'])
def modificar(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        curso.nombre = request.form.get('nombre')
        curso.descripcion = request.form.get('descripcion')
        curso.maestro_id = request.form.get('maestro_id')
        db.session.commit()
        return redirect(url_for('cursos.index'))
    maestros = Maestros.query.all()
    return render_template('cursos/modificar.html', curso=curso, maestros=maestros)

@cursos.route("/cursos/eliminar/<int:id>", methods=['GET', 'POST'])
def eliminar(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        curso.alumnos = [] 
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template('cursos/eliminar.html', curso=curso)


@cursos.route("/cursos/detalles/<int:id>")
def detalles(id):
    curso_obj = Curso.query.get_or_404(id)
    return render_template('cursos/detalles.html', curso=curso_obj)







