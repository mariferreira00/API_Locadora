def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }


def diretor_from_db(*args):
         return [{"nome_completo": diretor[0][1]} for diretor in args]



def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }

def genero_from_db(*args):
    return [{"nome": genero[0][1]} for genero in args]

def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }

def filme_from_db(*args):
    return [{
        "titulo": filme[0][1],
        "ano": filme[0][1],
        "classificacao": filme[0][1],
        "preco": filme[0][1],
        "diretores_id": filme[0][1],
        "generos_id": filme[0][1]
    } for filme in args]


def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
        "CPF": kwargs["CPF"] if kwargs["CPF"] else ""
    }


def usuario_from_db(usuario):
    return{
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"],
    }


def delete_id_from_web(**kwargs):
    return {
        "id": kwargs["id"] if kwargs["id"] else ""
    }
def delete_id_from_db(*args):
    return [{
        "id": id[0][1]
    } for id in args]

def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


def delete_id_from_db(*args):
    return {
        "id": args[0]
    }

def locacao_from_web(**kwargs):
    return {
        "data_inicio": kwargs["data_inicio"] if "data_inicio" in kwargs else "",
        "data_fim": kwargs["data_fim"] if "data_fim" in kwargs else "",
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "id_usuario": kwargs["id_usuario"] if "id_usuario" in kwargs else "",
    }

def locacao_from_db(args):
    return {
        "id": args["id"],
        "data_inicio": args["data_inicio"],
        "data_fim": args["data_fim"],
        "filmes_id": args["filmes_id"],
        "id_usuario": args["id_usuario"],
    }
def id_locacoes_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""

def pagamento_from_web(**kwargs):
    return{
        "tipo": kwargs["tipo"] if "tipo" in kwargs else "",
        "status": kwargs["status"] if "status" in kwargs else "",
        "codigo_pagamento": kwargs["codigo_pagamento"] if "codigo_pagamento" in kwargs else "",
        "valor": kwargs["valor"] if "valor" in kwargs else "",
        "data": kwargs["data"] if "data" in kwargs else "",
    }

def pagamento_from_db(args):
    return {
        "id": args["id"],
        "tipo": args["tipo"],
        "status": args["status"],
        "codigo_pagamento": args["codigo_pagamento"],
        "valor": str(args["valor"]),
        "data": args["data"],
        "locacoes_id": args["locacoes_id"],

    }
def id_pagamentos_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""
    if id_usuario == 0:
        return False
    return True