import Connection.ConnectionDB
from Connection import ConnectionDB

with open('C:/Users/sebas/Pictures/Screenshots/Sesion5.pdf', 'rb') as f:
    data = f.read()

conecion = ConnectionDB.Connection().insertFiles3(data)


