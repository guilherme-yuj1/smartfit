from models.aluno_models import Aluno
from db import db
import json
from flask import make_response

def get_alunos():
    alunos = Aluno.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de alunos.',
            'dados': [aluno.json() for aluno in alunos]
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


def get_aluno_by_id(aluno_id):
    aluno = Aluno.query.get(aluno_id)

    if aluno:
        response = make_response(
            json.dumps({
                'mensagem': 'Aluno encontrado.',
                'dados': aluno.json()
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({'mensagem': 'Aluno não encontrado.', 'dados': {}}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response


def create_aluno(aluno_data):
    if not all(key in aluno_data for key in ['nome', 'cpf', 'idade']):
        response = make_response(
            json.dumps(
                {'mensagem': 'Dados inválidos. Nome, CPF e idade são obrigatórios.'},
                ensure_ascii=False
            ),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        cpf=aluno_data['cpf'],
        idade=aluno_data['idade']
    )

    db.session.add(novo_aluno)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Aluno cadastrado com sucesso.',
            'aluno': novo_aluno.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


def update_aluno(aluno_id, aluno_data):
    aluno = Aluno.query.get(aluno_id)

    if not aluno:
        response = make_response(
            json.dumps({'mensagem': 'Aluno não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    if not all(key in aluno_data for key in ['nome', 'cpf', 'idade']):
        response = make_response(
            json.dumps(
                {'mensagem': 'Dados inválidos. Nome, CPF e idade são obrigatórios.'},
                ensure_ascii=False
            ),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    aluno.nome = aluno_data['nome']
    aluno.cpf = aluno_data['cpf']
    aluno.idade = aluno_data['idade']

    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Aluno atualizado com sucesso.',
            'aluno': aluno.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


def delete_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)

    if not aluno:
        response = make_response(
            json.dumps(
                {'mensagem': 'Aluno não encontrado.'},
                ensure_ascii=False
            ),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(aluno)
    db.session.commit()

    response = make_response(
        json.dumps(
            {'mensagem': 'Aluno deletado com sucesso.'},
            ensure_ascii=False
        ),
        200
    )

    response.headers['Content-Type'] = 'application/json'
    return response