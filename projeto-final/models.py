from comandos_bd import insert, update, delete, select



def insert_diretor(nome_completo):
    insert("diretores", ["nome_completo"], [nome_completo])


def insert_genero(nome):
    insert("generos", ["nome"], [nome])


def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def insert_usuario(nome_completo, CPF):
    insert("usuarios", ["nome_completo", "CPF"],
           [nome_completo, CPF])


def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["nome_completo"], [nome_completo])


def update_genero(id, nome):
    update("generos", "id", id, ["nome"], [nome])


def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])


def update_usuario(id, nome_completo, CPF):
    update("usuarios", "id", id, ["nome_completo", "CPF"], [nome_completo, CPF])


def delete_diretor(id):
    delete("diretores", "id", id)


def delete_genero(id):
    delete("generos", "id", id)


def delete_filme(id):
    delete("filmes", "id", id)


def delete_usuario(id):
    delete("usuarios", "id", id)

def select_usuarios(nome_completo):
    return select("usuarios", "nome_completo", nome_completo)

def select_diretor(nome_completo):
    select("diretores", "nome_completo", nome_completo)



def get_diretor(nome_completo):
    select("diretores", "nome_completo", nome_completo)