from app import app
from db import db
from aluno_models import Aluno

alunos_dados = [
    {"nome": "Neymar Jr", "cpf": "34728920104", "idade": 34},
    {"nome": "Vinícius Jr", "cpf": "83928395821", "idade": 26}
    {"nome": "Raphael Dias", "cpf": "02938754323", "idade": 29}
    {"nome": "Bruno Guimarães", "cpf": "32093848939", "idade": 28}
    {"nome": "Marcos Aoás", "cpf": "21290348726", "idade": 32}
]

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        cpfs = {a.cpf for a in Aluno.query.all()}
        inserir = [s for s in alunos_dados if s["cpf"] not in cpfs]
        if inserir:
            alunos = [Aluno(nome=s["nome"], cpf=s["cpf"],
                            idade=s["idade"]) for s in inserir]
            db.session.add_all(alunos)
            db.session.commit()
            print(f"Inserido {len(inserir)} alunos.")
        else:
            print("Nenhum aluno novo para inserir.")
