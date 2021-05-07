from flask import Flask, jsonify, request
from serializadores import diretor_from_web, diretor_from_db, genero_from_web, genero_from_db, filme_from_web, \
    filme_from_db, usuario_from_db, usuario_from_web, delete_id_from_web, delete_id_from_db, nome_usuario_from_web
from validacao import validacao_diretor, validacao_genero, validacao_filme, validacao_usuario, validacao_id
from models import insert_diretor, insert_genero, insert_filme, insert_usuario, update_diretor, update_genero, \
    update_filme, update_usuario, delete_diretor, delete_genero, delete_filme, delete_usuario, select_diretor, \
    get_diretor, select_usuarios


app = Flask(__name__)


@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if validacao_diretor(**diretor):
        insert_diretor(**diretor)
        # diretor_inserido = get_diretor(diretor["nome_completo"])
        return jsonify(diretor_from_db(diretor))
    else:
        return jsonify({"erro": "Diretor Inválido."})


@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if validacao_genero(**genero):
        insert_genero(**genero)
        return jsonify(genero_from_db(genero))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível inserir esse Gênero, tente novamente!"})


@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if validacao_filme(**filme):
        insert_filme(**filme)
        return jsonify(filme_from_db(filme))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível inserir este filme, tente novamente!"})


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if validacao_usuario(**usuario):
        insert_usuario(**usuario)
        return jsonify(usuario_from_db(usuario))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível inserir este usuário, tente novamente!"})



@app.route("/diretores/<int:id>", methods=["PUT"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if validacao_id(id):
        update_diretor(id, **diretor)
        return jsonify(diretor_from_db(diretor))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível fazer esta alteração, tente novamente!"})


@app.route("/generos/<int:id>", methods=["PUT"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if validacao_id(id):
        update_genero(id, **genero)
        return jsonify(genero_from_db(genero))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível fazer esta alteração, tente novamente!"})

@app.route("/filmes/<int:id>", methods=["PUT"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if validacao_id(id):
        update_filme(id, **filme)
        return jsonify(filme_from_db(filme))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível fazer esta alteração, tente novamente!"})

@app.route("/usuarios/<int:id>", methods=["PUT"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if validacao_id(id):
        update_usuario(id, **usuario)
        return jsonify(usuario_from_db(usuario))
    else:
        return jsonify({"erro": "Usuário Inálido"})


@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    diretor_id = delete_id_from_web(**request.json)
    try:
        if validacao_id(id):
            delete_diretor(**diretor_id)
            return jsonify(delete_id_from_db(diretor_id))
    except:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível apagar o objeto selecionado!"})


@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    genero_id = delete_id_from_web(**request.json)
    try:
        if validacao_id(id):
            delete_genero(**genero_id)
            return jsonify(delete_id_from_db(genero_id))
    except:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível apagar o objeto selecionado!"})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    filme_id = delete_id_from_web(**request.json)
    try:
        if validacao_id(id):
            delete_filme(**filme_id)
            return jsonify(delete_id_from_db(filme_id))
    except:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível apagar o objeto selecionado!"})


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return None, 204
    except:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível apagar o objeto selecionado!"})


@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)



@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretor_from_web(**request.json) # pegar o diretor da web
    select_diretor(**diretor)
    diretor_selecionado = get_diretor(diretor["nome_completo"])
    if diretor_selecionado != None:
        return jsonify(diretor_from_db(diretor_selecionado))
    elif diretor_selecionado == None:
        return jsonify({"erro": "Ops algo deu errado ... Não encontramos nenhum resultado para sua busca, tente novamente!"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)