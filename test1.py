import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import mimetypes

load_dotenv()

con = os.getenv("senha")

remetente = "lipegfelix@gmail.com"
destinatario = "lipegfelix@gmail.com"
assunto = "Seu relatório chegou!"
mensagem = """
Olá, aqui está o relatório com os dados de vendas

ass, Felix
"""

senha = con
anexo = "./imagetest.jpg"

msg = EmailMessage()
msg["From"] = remetente
msg["To"] = destinatario
msg["Subject"] = assunto
msg.set_content(mensagem)

mime_type, _ = mimetypes.guess_type(anexo)
mime_type, mime_subtype = mime_type.split("/")

with open(anexo, "rb") as arquivo:
    msg.add_attachment(arquivo.read(), maintype=mime_type, subtype=mime_subtype, filename=anexo)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
    email.login(remetente,senha)
    email.send_message(msg)

print("Email foi enviado com sucesso!")