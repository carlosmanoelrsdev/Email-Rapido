import os
from dotenv import load_dotenv
from configJSON import LerJson

load_dotenv()

def PegarGmail(): # Descontinuada, use PegarGmailJSON
    MAIL_SERVIDOR = os.getenv("MAIL_SERVIDOR_GMAIL")
    MAIL_USER = os.getenv("MAIL_USER_GMAIL")
    MAIL_SENHA = os.getenv("MAIL_SENHA_GMAIL")
    return MAIL_SERVIDOR, MAIL_USER, MAIL_SENHA

def PegarNumero():
    NUMERO_TELEFONE = os.getenv("NUMERO_TELEFONE")
    return NUMERO_TELEFONE

def PegarGmailJSON(id):
    MAIL_SERVIDOR = LerJson(id)[0]
    MAIL_USER = LerJson(id)[1]
    MAIL_SENHA = LerJson(id)[2]
    return MAIL_SERVIDOR, MAIL_USER, MAIL_SENHA

