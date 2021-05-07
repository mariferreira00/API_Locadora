def validacao_diretor(nome_completo):

    if len(nome_completo) == 0:
        return False

    return True

def validacao_genero(nome):

    if len(nome) == 0:
        return False

    return True

def validacao_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):

    if len(titulo) == 0:
        return False

    elif ano == 0:
        return False

    elif int(classificacao) < 0 or int(classificacao) > 18:
        return False

    elif preco == 0:
        return False

    elif diretores_id == 0:
        return False

    elif generos_id == 0:
        return False

    return True


def validacao_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True


def validacao_id(id):

    if id == 0:
        return False

    return True