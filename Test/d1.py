# import Connection.ConnectionDB
# from Connection import ConnectionDB
#
# with open('C:/Users/sebas/Pictures/Screenshots/Sesion5.pdf', 'rb') as f:
#     data = f.read()
#
# conecion = ConnectionDB.Connection().insertFiles3(data)

import time
tiempo = 21
restante = 1
while tiempo != 0:
    time.sleep(1)
    tiempo = tiempo - restante
    print(tiempo)
if tiempo == 0:
    print("Tiempo acabado")
