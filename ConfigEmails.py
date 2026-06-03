from imap_tools import AND, MailBox
from EnvioWhatsapp import EntrarWhatsapp, FormatarEmailsParaWhatsapp
from config import PegarGmail
import datetime

emails_do_dia = []

def SalvarData():
    with open("email.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("Emails Dia: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\n\n")

def FinalizarEmail():
    with open("email.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("Final dos emails\n")
        arquivo.write("-" * 50 + "\n\n")

def SalvarMemoriaTemporario(mensagem):
    email_dict = {
        "remetente": mensagem.from_,
        "assunto": mensagem.subject,
        "data": mensagem.date.strftime('%d/%m/%Y %H:%M'),
        "conteudo": " ".join(mensagem.text.split())[:150]
    }
    emails_do_dia.append(email_dict)
    return email_dict

def SalvarEmail(mensagem):
    with open("email.txt", "a", encoding="utf-8") as arquivo:
    
        arquivo.write(f"\nDe: {mensagem.from_}\n")

        arquivo.write(f"Assunto: {mensagem.subject}\n")

        arquivo.write(f"Data: {mensagem.date.strftime('%d/%m/%Y %H:%M')}\n")
        
        texto = " ".join(mensagem.text.split())
        conteudo = f"CONTEÚDO: {texto[:150]}...\n\n"
        arquivo.write(conteudo)

def contagemEmails(quantidade):
    with open("email.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Quantidade de emails: {quantidade}\n")

def ConectarEmail(MAIL_SERVIDOR, MAIL_USER, MAIL_SENHA):
    global emails_do_dia
    emails_do_dia.clear()

    SalvarData()

    with MailBox(MAIL_SERVIDOR).login(MAIL_USER, MAIL_SENHA) as mb:
        NovasMensagens = False
        quantidadeMensagens = 0

        for mensagem in mb.fetch(AND(seen=False), reverse=True, mark_seen=True):
            NovasMensagens = True
            
            if mensagem.from_ == "no-reply@accounts.google.com":
                continue

            SalvarMemoriaTemporario(mensagem)
            SalvarEmail(mensagem)
        
            quantidadeMensagens += 1
            
        if not NovasMensagens:
            print("Nenhum email novo encontrado.")

        contagemEmails(quantidadeMensagens)

    FinalizarEmail()

    print("Quantidade de emails encontrados: " + str(quantidadeMensagens))

    return emails_do_dia

def Main():
    print("Contas Localizadas: Gmail")
    print("Gmail: " + PegarGmail()[1])
    print("Conectando ao Gmail...")
    try:
        MAIL_SERVIDOR, MAIL_USER, MAIL_SENHA = PegarGmail()
        emails_capturados = ConectarEmail(MAIL_SERVIDOR, MAIL_USER, MAIL_SENHA)
        print(f"\n# TOTAL: {len(emails_capturados)} emails prontos para enviar ao WhatsApp")

        EntrarWhatsapp(FormatarEmailsParaWhatsapp(emails_capturados))

    except Exception as e:
        print(f"Erro ao obter credenciais do Gmail: {e}\nVerifique a Rede ou as variáveis de ambiente.")
        print("Encerrando o programa.")
        return
