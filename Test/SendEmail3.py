import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
parte_html = MIMEText(html, "html")

# Agregar contenido al mensaje
mensaje.attach(parte_html)
archivo = "aqui va el adjunto"

with open(archivo, "rb") as adjunto:
    contenido_adjunto = MIMEBase("application", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename = {archivo}",
)

mensaje.attach(contenido_adjunto)
text = mensaje.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email, password)
    server.sendmail(email, destinatario, text)