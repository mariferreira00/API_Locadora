from comandos_bd import insert, update, delete, select, select_like



def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def get_diretor(id):
    return select("diretores", "id", id)

def insert_genero(nome):
    return insert("genero", ["nome"], [nome])

def get_genero(id):
    return select("genero", "id", id)


def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def get_filme(id):
    return select("filmes", "id", id)


def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"],
           [nome_completo, CPF])

def get_usuario(id):
    return select("usuarios", "id", id)

def update_diretor(id, nome_completo):
   return update("diretores", "id", id, ["nome_completo"], [nome_completo])


def update_genero(id, nome):
    return update("generos", "id", id, ["nome"], [nome])

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
    return select_like("diretores", "nome_completo", f"%{nome_completo}%")

def select_genero(nome):
    return select_like("generos", "nome", f"%{nome}%")

def select_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return select_like("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [f"""%{titulo}%,
        %{ano}%, %{classificacao, preco, diretores_id, generos_id}%"""])

def select_usuario(nome_completo, CPF):
    return select_like("diretores", ["nome_completo", "CPF"], [f"%{nome_completo}%", f"%{CPF}%"])
