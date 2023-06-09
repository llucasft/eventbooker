from flask import render_template, session, redirect, request, flash, url_for

from main import app, db
from models import Usuario, Evento, Participante

@app.route('/')
def index():
    eventos = Evento.query.order_by(Evento.id)
    return render_template('list.html', eventos=eventos)

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/auth', methods=['POST',])
def auth():
    usuario = Usuario.query.filter_by(email=request.form['email']).first()
    if usuario:
        if request.form['password'] == usuario.senha:
            session['logged_user'] = usuario.nome
            flash(usuario.nome + 'Logado com sucesso!')
            next_page = request.form['next']
            return redirect(next_page)
        else:
            flash('Não foi possível efetuar o login.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/new')
def new_event():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('new_event')))
    return render_template('new.html')

@app.route('/create', methods=['POST',])
def create():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    local = request.form['local']
    data = request.form['data']
    horario = request.form['hora']

    evento = Evento.query.filter_by(titulo=titulo).first()

    if evento:
        flash("Título já existente, favor escolher outro.")
        return redirect(url_for('index'))
    
    novo_evento = Evento(titulo=titulo, descricao=descricao, local_evento=local, data_evento=data, hora=horario, id_usuario=1)
    db.session.add(novo_evento)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('edit')))
    
    evento = Evento.query.filter_by(id=id).first()
    return render_template('edit.html', titulo='Editando evento', evento=evento)

@app.route('/update', methods=['POST',])
def update():
    pass

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))