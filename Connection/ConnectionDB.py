import mysql.connector
from mysql.connector import Error


class Connection:
    def startConnection(self):
        try:
            conexion = mysql.connector.connect(
                user="root",
                password="sebas2001",
                host="localhost",
                database="python",
                port="3306")
            return conexion
        except Error:
            print("Error de conexión")

    def listUser(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM user")
        resultado = cursor.fetchall()
        for r in resultado:
            print(r[0], r[1], r[2], r[3])
        conexion.close()

    def validateUser(self, email, password):
        conexion = self.startConnection()
        flagType = None
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT flagType FROM user WHERE email='" + email + "' AND password='" + password + "'")
        resultado = cursor.fetchone()
        if resultado:
            if resultado[0] == 0:
                flagType = 0
            elif resultado[0] == 1:
                flagType = 1
        else:
            print("No existe el usuario")
        conexion.close()
        return flagType

    def getDataUserStudent(self, email, password):
        conexion = self.startConnection()
        valores = None
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT s.name, s.lastName, u.flagType FROM user AS u "
            "INNER JOIN student AS s ON (s.idUser = u.idUser)"
            "WHERE u.email='" + email + "' AND u.password='" + password + "'")

        resultado = cursor.fetchall()
        for n in resultado:
            valores = n[0] + " " + n[1]
        conexion.close()
        return valores

    def getDataUserTeacher(self, email, password):
        conexion = self.startConnection()
        valores = None
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT t.name, t.lastName, u.flagType FROM user AS u "
            "INNER JOIN teacher AS t ON (t.idUser = u.idUser)"
            "WHERE u.email='" + email + "' AND u.password='" + password + "'")

        resultado = cursor.fetchall()
        for n in resultado:
            valores = n[0] + " " + n[1]
        conexion.close()
        return valores

    def insertUser_Student(self, name, lastname, age, degree, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO student (name, lastName, age, degree, idUser) VALUES ('{}', '{}', '{}', '{}', '{}')" \
            .format(name, lastname, age, degree, idUser)
        cursor.execute(sql)
        conexion.commit()
        print("Ingreso exitoso estudiante")
        conexion.close()

    def insertUser_Teacher(self, name, lastName, cellphone, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO teacher (name, lastName, cellphone, idUser) VALUES ('{}', '{}', '{}', '{}')" \
            .format(name, lastName, cellphone, idUser)
        cursor.execute(sql)
        conexion.commit()
        print("Ingreso exitoso teacher")
        conexion.close()

    def insertUser(self, email, password, flagType):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO user (email, password, flagType) VALUES ('{}', '{}', '{}')".format(email, password, flagType)
        cursor.execute(sql)
        conexion.commit()
        print("Ingreso exitoso user")
        conexion.close()

    def getLastIdUser(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT idUser FROM user ORDER BY idUser DESC")
        resultado = cursor.fetchone()[0]
        conexion.close()
        return resultado
