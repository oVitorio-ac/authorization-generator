import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from dotenv import load_dotenv

load_dotenv()

REMETENTE = str(os.environ.get('REMETENTE'))
SENHA = str(os.environ.get('SENHA'))
SERVIDOR = str(os.environ.get('SERVIDOR'))
porta = os.environ.get('PORTA')
PORTA = int(porta) if porta is not None else 587

def enviar_email(destinatario, assunto, corpo, arquivo_anexo):
    # Configurações do servidor SMTP
    servidor_smtp = SERVIDOR
    porta_smtp = PORTA  # Porta SMTP para conexão segura

    # Criando o objeto do e-mail
    msg = MIMEMultipart()
    msg['From'] = REMETENTE
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Adicionando o arquivo PDF como anexo
    with open(arquivo_anexo, 'rb') as anexo:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(anexo.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {arquivo_anexo}')
        msg.attach(part)

    # Estabelecendo conexão com o servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()
    servidor.login(REMETENTE, SENHA)

    # Enviando o e-mail
    texto_email = msg.as_string()
    servidor.sendmail(REMETENTE, destinatario, texto_email)

    # Encerrando a conexão
    servidor.quit()


