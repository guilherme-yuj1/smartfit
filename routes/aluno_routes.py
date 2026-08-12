from flask import Blueprint, request
from controllers.aluno_controllers import (
    get_alunos, create_aluno, update_aluno, get_aluno_by_id, delete_aluno)

aluno_routes = Blueprint('aluno_routes', __name__)


@aluno_routes.route('/Aluno', methods=['GET'])
def alunos_get():
    return get_alunos()


@aluno_routes.route('/Aluno/<int:aluno_id>', methods=['GET'])
def aluno_get_by_id(aluno_id):
    return get_aluno_by_id(aluno_id)


@aluno_routes.route('/Aluno', methods=['POST'])
def alunos_post():
    return create_aluno(request.json)


@aluno_routes.route('/Aluno/<int:aluno_id>', methods=['PUT'])
def alunos_put(aluno_id):
    return update_aluno(aluno_id, request.json)


@aluno_routes.route('/Aluno/<int:aluno_id>', methods=['DELETE'])
def alunos_delete(aluno_id):
    return delete_aluno(aluno_id)
