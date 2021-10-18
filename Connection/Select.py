import ConnectionDB


def listar():
    objUsuarios = ConnectionDB.Connection()
    objUsuarios.listUser()


listar()
