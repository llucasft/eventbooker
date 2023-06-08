from main import db

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