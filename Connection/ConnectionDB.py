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

    # === Methods Login ===
    def validateUser(self, email, password):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM user WHERE email='" + email + "' AND password='" + password + "'")
        result = False
        user = cursor.fetchone()
        if user:
            result = True
        elif not user:
            result = False
        conexion.close()
        return user, result

    def getDataUserStudent(self, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "SELECT * FROM student AS s INNER JOIN user AS u ON (s.idUser = u.idUser) WHERE u.idUser='" + idUser + "'"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        conexion.close()
        return resultado

    def getDataUserTeacher(self, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "SELECT * FROM teacher AS t INNER JOIN user AS u ON (t.idUser = u.idUser) WHERE u.idUser='" + idUser + "'"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        conexion.close()
        return resultado

    # === Methods Register ===
    def insertUser(self, email, password, avatar, code, flagType):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO user (email, password, avatar, code, flagType) VALUES ('{}','{}', '{}', '{}', '{}')" \
            .format(email, password, avatar, code, flagType)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def getLastIdUser(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT idUser FROM user ORDER BY idUser DESC")
        resultado = cursor.fetchone()[0]
        conexion.close()
        return resultado

    def insertUser_Student(self, name, lastname, age, degree, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO student (name, lastName, age, degree, idUser) VALUES ('{}', '{}', '{}', '{}', '{}')" \
            .format(name, lastname, age, degree, idUser)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def insertUser_Teacher(self, name, lastName, cellphone, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO teacher (name, lastName, cellphone, idUser) VALUES ('{}', '{}', '{}', '{}')" \
            .format(name, lastName, cellphone, idUser)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    # === List Students ===
    def listStudent4(self, code):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT s.name, s.lastName, s.age, u.email FROM student AS s INNER JOIN user AS u ON (s.idUser = u.idUser)"
            " WHERE u.code = '" + code + "' and s.degree = '4toº Primaria'")
        results = cursor.fetchall()
        quantity = cursor.rowcount
        print(results)
        conexion.close()
        return results, quantity

    def listStudent5(self, code):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT s.name, s.lastName, s.age, u.email FROM student AS s INNER JOIN user AS u ON (s.idUser = u.idUser)"
            " WHERE u.code = '" + code + "' and s.degree ='5toº Primaria'")
        results = cursor.fetchall()
        quantity = cursor.rowcount
        conexion.close()
        return results, quantity

    def listStudent6(self, code):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT s.name, s.lastName, s.age, u.email FROM student AS s INNER JOIN user AS u ON (s.idUser = u.idUser)"
            " WHERE u.code = '" + code + "' and s.degree = '6toº Primaria'")
        results = cursor.fetchall()
        print(results)
        conexion.close()
        return results

    # === Files ===
    def insertFile(self, urlFile, name, description, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO file (urlFile, name, description, idUser) VALUES ('{}', '{}', '{}', '{}')" \
            .format(urlFile, name, description, idUser)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def listFile(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM file")
        results = cursor.fetchall()
        quantity = cursor.rowcount
        conexion.close()
        return results, quantity

    # === Questions ===
    def insertQuestions(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, idUser):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = "INSERT INTO form (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, idUser) VALUES ('{}', '{}', '{}', '{}', " \
              "'{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, idUser)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def insertFiles2(self, pdf):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        sql = """INSERT INTO test (pdf) VALUES (%s)"""
        cursor.execute(sql, (pdf,))
        conexion.commit()
        conexion.close()

    def listFile22(self):
        conexion = self.startConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()
        quantity = cursor.rowcount
        conexion.close()
        return results, quantity
