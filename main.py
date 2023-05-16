from flask import Flask, render_template, session, redirect, request, flash, url_for

class Event:
    def __init__(self, name, category, address):
        self.name=name
        self.category=category
        self.address=address

event1 = Event('Reunião de vizinhos', 'Reunião', 'Auditório do condomínio')
event2 = Event('Culto de Páscoa', 'Culto', 'Igreja Batista')
event3 = Event('Show do Luan', 'Show', 'Praça central')

events = [event1, event2, event3]

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

user1 = User("Bruno Divino", "BD", "alohomora")
user2 = User("Lucas Ferreira", "lucas", "1234")
user3 = User("Guilherme Louro", "Cake", "python_eh_vida")

users = { user1.username : user1,
             user2.username : user2,
             user3.username : user3 }

app = Flask(__name__)
app.secret_key = 'eventbooker'

@app.route('/')
def index():
    return render_template('list.html', events=events)

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