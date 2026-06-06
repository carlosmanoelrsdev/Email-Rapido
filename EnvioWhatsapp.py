import pyautogui as pg
import pyperclip
from config import PegarNumero

def FormatarEmailsParaWhatsapp(emails_array):

    mensagem_formatada = f"Emails do dia:\n\n"
    if not emails_array:
        return "Nenhum email encontrado para hoje."
    
    for idx, email in enumerate(emails_array, 1):
        mensagem_formatada += f"Email: {email['emailRecebedor']}\n\n"
        mensagem_formatada += f"{idx}. De: {email['remetente']}\n\n"
        mensagem_formatada += f"   Assunto: {email['assunto']}\n\n"
        mensagem_formatada += f"   Data: {email['data']}\n\n"
        mensagem_formatada += f"   Conteudo: {email['conteudo']}...\n\n\n"
    
    return mensagem_formatada

def EntrarWhatsapp(mensagem_formatada):
    
    pg.sleep(1)
    pg.press("win")
    pg.write("edge")
    pg.hotkey("shift", "enter")

    pg.sleep(2)
    pg.write(f"https://web.whatsapp.com/send?phone={PegarNumero()}")
    pg.press("enter")

    pg.sleep(20)
    pyperclip.copy(mensagem_formatada)
    pg.hotkey("ctrl", "v")
    pg.sleep(2)
    pg.press("enter")
