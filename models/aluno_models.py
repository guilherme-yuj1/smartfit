from db import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(80), nullable=False, unique=True)
    idade = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'idade': self.idade
        }