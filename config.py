import os
from dotenv import load_dotenv

load_dotenv()

def PegarGmail():
    MAIL_SERVIDOR = os.getenv("MAIL_SERVIDOR_GMAIL")
    MAIL_USER = os.getenv("MAIL_USER_GMAIL")
    MAIL_SENHA = os.getenv("MAIL_SENHA_GMAIL")
    return MAIL_SERVIDOR, MAIL_USER, MAIL_SENHA

def PegarNumero():
    NUMERO_TELEFONE = os.getenv("NUMERO_TELEFONE")
    return NUMERO_TELEFONE