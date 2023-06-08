from flask import Flask, render_template, session, redirect, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'eventbooker'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:26Lucas.@localhost:5432/eventbooker'

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Evento(db.Model):
    __tablename__ = 'eventos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_evento = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time)
    local_evento = db.Column(db.Text, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Participante(db.Model):
    __tablename__ = 'participantes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    id_evento = db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' % self.name

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
    if request.form['username'] in users :
        user = users[request.form['username']]
        if request.form['password'] == user.password:
            session['logged_user'] = user.username
            flash(user.username + 'Logado com sucesso!')
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
    name = request.form['name']
    category = request.form['category']
    address = request.form['address']
    event = Event(name, category, address)
    events.append(event)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

app.run(debug=True)