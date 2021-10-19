import ConnectionDB


def listar():
    objUsuarios = ConnectionDB.Connection()
    objUsuarios.listFile()


listar()
