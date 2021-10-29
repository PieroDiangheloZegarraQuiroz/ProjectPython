import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Pedir datos
email = input("Ingrese su correo: ")
password = input("Ingrese su password: ")

destinatario = input("Ingrese el destinatario: ")
asunto = input("Ingrese el asunto: ")

# Crear el mensaje
mensaje = MIMEMultipart("alternativa")  # estandar
mensaje["Subject"] = asunto
mensaje["From"] = email
mensaje["To"] = destinatario

html = f""""
<html>
<body>
Hola {destinatario} <br>
Esto es un asunto de <b>{asunto}</b>
</body>
</html>
"""

# El contenido del mensaje como HTML
parte_html = MIMEText(html, "html")  # Indicamos la variable y el tipo

# Agregar contenido al mensaje
mensaje.attach(parte_html)

# Enviar el mensaje
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email, password)
    server.sendmail(email, destinatario, mensaje.as_string())
