import getpass
import smtplib
import ssl

username = input("Ingresa su correo: ")
password = input("Ingresa su password: ")

# Crea conexión
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("Inicio de sesión exitoso")
    destinatario = input("Ingrese el correo del destinatario: ")
    mensaje = input("Ingrese el mensaje: ")
    server.sendmail(username, destinatario, mensaje)
    print("Mensaje enviado")


