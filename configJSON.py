import json

def LerJson(id):
    with open("emails.json", "r", encoding="utf-8") as arquivo:
        dados_emails = json.load(arquivo)
        lista_emails = dados_emails["emails"]

        while True:
            try:
                servidor = lista_emails[id]["servidor"] 
                conta = lista_emails[id]["email"]
                senha = lista_emails[id]["senhaAPP"]
                return servidor, conta, senha
            except IndexError:
                return "ID não encontrado"
        

def QuantidadeEmails():
    with open("emails.json", "r", encoding="utf-8") as arquivo:
        dados_emails = json.load(arquivo)
        lista_emails = dados_emails["emails"]
        return len(lista_emails) - 1
    
def MostrarEmails():
    with open("emails.json", "r", encoding="utf-8") as arquivo:
        dados_emails = json.load(arquivo)
        lista_emails = dados_emails["emails"]
        for email in lista_emails:
            print(f"ID: {email['ID']} - Email: {email['email']}")

    