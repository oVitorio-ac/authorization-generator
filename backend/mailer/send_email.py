import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

REMETENTE = str(os.environ.get("REMETENTE"))
SENHA = str(os.environ.get("SENHA"))
SERVIDOR = str(os.environ.get("SERVIDOR"))
porta = os.environ.get("PORTA")
PORTA = int(porta) if porta is not None else 587


def enviar_email(destinatario, assunto, corpo, arquivo_anexo):
    # Configurações do servidor SMTP
    servidor_smtp = SERVIDOR
    porta_smtp = PORTA  # Porta SMTP para conexão segura

    # Criando o objeto do e-mail
    msg = MIMEMultipart()
    msg["From"] = REMETENTE
    msg["To"] = destinatario
    msg["Subject"] = assunto

    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo, "plain"))

    part = MIMEBase("application", "octet-stream")
    part.set_payload(arquivo_anexo.getvalue())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition", f"attachment; filename=autorizacao_desbravadores.pdf"
    )
    msg.attach(part)

    # Estabelecendo conexão com o servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()
    servidor.login(REMETENTE, SENHA)

    # Enviando o e-mail
    servidor.sendmail(REMETENTE, destinatario, msg.as_string())

    # Encerrando a conexão
    servidor.quit()


# Exemplo de uso:
# buffer = BytesIO(b'seu conteúdo em bytes')
# enviar_email('destinatario@example.com', 'Assunto do Email', 'Corpo do Email', buffer, 'arquivo.pdf')
