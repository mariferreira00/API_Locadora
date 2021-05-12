from flask import Flask, jsonify, request, Response
from serializadores import diretor_from_web, diretor_from_db, genero_from_web, genero_from_db, filme_from_web, \
    filme_from_db, usuario_from_db, usuario_from_web, delete_id_from_web, delete_id_from_db, \
    locacao_from_web, locacao_from_db, id_locacoes_from_web,  pagamento_from_web, pagamento_from_db, id_pagamentos_from_web
from validacao import validacao_diretor, validacao_genero, validacao_filme, validacao_usuario, validacao_id, validacao_pagamento, validacao_locacao
from models import insert_diretor, insert_genero, insert_filme, insert_usuario, update_diretor, update_genero, \
    update_filme, update_usuario, delete_diretor, delete_genero, delete_filme, delete_usuario, select_diretor, \
    get_locacao, select_locacao, update_locacao, delete_locacoes, insert_pagamento, get_pagamento, select_pagamento, update_pagamento, \
    get_diretor, get_genero, get_filme, get_usuario, select_genero, select_filme, select_usuario, insert_locacao, get_locacao, delete_pagamentos
from datetime import timedelta, datetime



app = Flask(__name__)


@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if validacao_diretor(**diretor):
        id = insert_diretor(**diretor)
        diretor_inserido = get_diretor(diretor[id])
        return jsonify(diretor_from_db(diretor_inserido))
    else:
        return jsonify({"erro": "Diretor Inválido."})


@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if validacao_genero(**genero):
        id = insert_genero(**genero)
        genero_inserido = get_genero(genero[id])
        return jsonify(genero_from_db(genero_inserido))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível inserir esse Gênero, tente novamente!"})


@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if validacao_filme(**filme):
        insert_filme(**filme)
        return jsonify(filme_from_db(filme))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível inserir este filme"})


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if validacao_usuario(**usuario):
        id = insert_usuario(**usuario)
        usuario_inserido = get_usuario(id)
        return jsonify(usuario_from_db(usuario_inserido))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível inserir este usuario"})



@app.route("/diretores/<int:id>", methods=["PUT","PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if validacao_id(id):
        update_diretor(id, **diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_alterado), Response[201])
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível fazer esta alteração, tente novamente!"})


@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if validacao_id(id):
        update_genero(id, **genero)
        genero_alterado = get_genero(genero["nome"])
        return jsonify(genero_from_db(genero_alterado))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível fazer esta alteração, tente novamente!"})

@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if validacao_id(id):
        update_filme(id, **filme)
        filme_alterado = get_filme("titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id")
        return jsonify(filme_from_db(filme_alterado))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não foi possível fazer esta alteração, tente novamente!"})

@app.route("/usuarios/<int:id>", methods=["PUT","PATCH"])
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
            return jsonify(delete_id_from_db("", 204))
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
    usuario = usuario_from_web(**request.args)
    usuarios_selecionados = select_usuario(**usuario)
    if len(usuarios_selecionados) > 0:
        return jsonify(usuario_from_db(usuarios_selecionados))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Usuário não encontrado, tente novamente!."})


@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretor_from_web(**request.args)
    diretores_selecionados = select_diretor(**diretor)
    if len(diretores_selecionados) > 0:
        return jsonify(diretor_from_db(diretores_selecionados))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Não encontramos nenhum resultado para sua busca, tente novamente!"})

@app.route("/generos", methods=["GET"])
def buscar_genero():
    genero = genero_from_web(**request.args)
    generos_selecionados = select_genero(**genero)
    if len(generos_selecionados) > 0:
        return jsonify(genero_from_db(generos_selecionados))
    else:
        return jsonify({"erro":"Ops algo deu errado ... Gênero inválido, tente novamente!"})

@app.route("/filmes", methods=["GET"])
def buscar_filme():
    filme = filme_from_web(**request.args)
    filmes_selecionados = select_filme(**filme)
    if len(filmes_selecionados) > 0:
        return jsonify(filme_from_db(filmes_selecionados))
    else:
        return jsonify({"erro": "Ops algo deu errado ... Filme inválido, tente novamente!"})

@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)
    if validacao_locacao(**locacao):
        id_locacao = insert_locacao(**locacao)
        locacao_cadastrada = get_locacao(id_locacao)
        return locacao_from_db(locacao_cadastrada)
    else:
        return jsonify({"erro":"Ops algo deu errado... Não foi possível processar a sua solicitação! "})

@app.route("/locacoes", methods=["GET"])
def buscar_locacoes():
    locacao_id = id_locacoes_from_web(**request.json)
    locacoes = select_locacao(locacao_id)
    locacoes_from_db = [locacao_from_db(id) for id in locacoes]
    return jsonify(locacoes_from_db)

@app.route("/locacoes/<int:id>", methods=["PATCH", "PUT"])
def alterar_locacoes(id):
    locacao = locacao_from_web(**request.json)
    if validacao_locacao(**locacao):
        update_locacao(id, **locacao)
        locacao_cadastrada = get_locacao(id)
        return jsonify(locacao_from_db(locacao_cadastrada))
    else:
        return jsonify({"erro":"Ops, algo deu errado... Não foi possível prosseguir com esta locação!."})

@app.route("/locacoes/<int:id>", methods=["DELETE"])
def apagar_locacoes(id):
    try:
        delete_locacoes(id)
        return "", 204
    except:
        return jsonify({"erro":"Ops, algo deu errado, impossível deletar esta locação!."})

@app.route("/pagamentos", methods=["POST"])
def inserir_pagamento():
    pagamento = pagamento_from_web(**request.json)
    if validacao_pagamento(**pagamento):
        id_pagamento = insert_pagamento(**pagamento)
        pagamento_cadastrado = get_pagamento(id_pagamento)
        return pagamento_from_db(pagamento_cadastrado)
    else:
        return jsonify({"erro":"Pagamento Inválido."})

@app.route("/pagamentos", methods=["GET"])
def buscar_pagamentos():
    pagamento_id = id_pagamentos_from_web(**request.json)
    pagamentos = select_pagamento(pagamento_id)
    pagamentos_from_db = [pagamento_from_db(id) for id in pagamentos]
    return jsonify(pagamentos_from_db)

@app.route("/pagamentos/<int:id>", methods=["PATCH", "PUT"])
def altera_pagamento(id):
    pagamento = pagamento_from_web(**request.json)
    if validacao_pagamento(**pagamento):
        update_pagamento(id, **pagamento)
        pagamento_cadastrado = get_pagamento(id)
        return jsonify(pagamento_from_db(pagamento_cadastrado))
    else:
        return jsonify({"erro":"Ops algo deu errado... Não foi possível processar este pagamento."})

@app.route("/pagamentos/<int:id>", methods=["DELETE"])
def apagar_pagamentos(id):
    try:
        delete_pagamentos(id)
        return "", 204
    except:
        return jsonify({"erro":"Ops algo deu errado... Não foi possível deletar este pagamento!."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
