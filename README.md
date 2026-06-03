# Email Rápido - Gerenciador de Emails no WhatsApp

 **Aplicativo Desktop para receber emails direto no WhatsApp de forma simples, automática e intuitiva, com salvamento em .txt para backups futuros.**

---

## Sobre o Projeto

O **Email Rápido** é um projeto pessoal para organizar e automatizar a leitura de emails. A aplicação resolve um problema real: falta de organização dos emails ou esquecimento de verificar diariamente.

### Objetivo

Entregar uma aplicação funcional e clara que ajude na leitura dos emails diários com as seguintes funcionalidades:

- Conexão com Gmail automática via IMAP
- Salvamento em formato `.txt` para backup
- Automação WhatsApp sem risco de bloqueio
- Extração de conteúdo relevante dos emails
- Formatação clara e organizada

---

## Estrutura do Projeto

```
TesteIMAP/
├── App.py                 # Ponto de entrada da aplicação
├── config.py              # Carregamento de variáveis de ambiente
├── ConfigEmails.py        # Lógica principal de conexão e leitura de emails
├── EnvioWhatsapp.py       # Automação de envio via WhatsApp Web
├── email.txt              # Arquivo de backup com emails (gerado)
├── .env                   # Variáveis de ambiente (não incluído no git)
├── .env.example           # Exemplo de variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo git
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## Instalação

### Pré-Requisitos

- **Python 3.10** ou superior
- **Gmail** com autenticação habilitada
- **Senha de Aplicativo Gmail** (App Password)
- **PyAutoGUI** funcionando corretamente no seu SO
- **Edge** instalado (para WhatsApp Web)

### Passo a Passo

#### 1. Clone o repositório

```bash
git clone https://github.com/carlosmanoelrsdev/Email-R-pido---Gerenciador-de-Emails-no-WhatsApp.git
```

#### 2. Crie e ative o ambiente virtual

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Windows)
.venv\Scripts\activate

# Ativar (Linux/Mac)
source .venv/bin/activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Abra o `.env` e configure com suas credenciais:

```env
MAIL_SERVIDOR_GMAIL=imap.gmail.com
MAIL_USER_GMAIL=seu.email@gmail.com
MAIL_SENHA_GMAIL=sua_senha_de_app_do_gmail
NUMERO_TELEFONE=Seu Número
```

#### 5. Obtenha a Senha de Aplicativo Gmail

1. Acesse [Google Account Security](https://myaccount.google.com/security)
2. Ative autenticação de dois fatores
3. Em "Senhas de aplicativo", gere uma nova senha
4. Use essa senha no arquivo `.env`

---

## Como Executar

```bash
python app.py
```

Após executar, o programa irá:
1. Conectar ao Gmail
2. Buscar emails do dia
3. Salvar em `email.txt`
4. Abrir WhatsApp Web automaticamente
5. Enviar os emails formatados via WhatsApp

---

## Fluxo de Uso

```
1. Iniciar aplicação (python app.py)
   ↓
2. Autenticar no Gmail com .env
   ↓
3. Buscar emails do dia (IMAP)
   ↓
4. Processar e formatar emails
   ↓
5. Salvar em email.txt (backup)
   ↓
6. Abrir WhatsApp Web
   ↓
7. Enviar mensagem formatada via automação
   ↓
8. Finalizar (log em email.txt)
```

---

## Arquitetura e Destaques Técnicos

### Componentes Principais

| Arquivo | Responsabilidade |
|---------|-----------------|
| **App.py** | Ponto de entrada, inicializa a aplicação |
| **config.py** | Carrega variáveis de ambiente do `.env` |
| **ConfigEmails.py** | Lógica IMAP, busca e processamento de emails |
| **EnvioWhatsapp.py** | Automação via PyAutoGUI e WhatsApp Web |

### Tecnologias Utilizadas

- **imap_tools**: Conexão e manipulação de emails via IMAP
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **pyautogui**: Automação de interface do sistema
- **pyperclip**: Manipulação da área de transferência

---

## Configuração Avançada

### Alterar Formato de Emails

Customize a função `FormatarEmailsParaWhatsapp()` em `EnvioWhatsapp.py` conforme necessário.

### Filtrar Emails Específicos

Modifique a lógica de busca em `ConfigEmails.py` para filtrar por remetente, assunto, etc.

---

## Troubleshooting

| Problema | Solução |
|----------|---------|
| Erro de autenticação Gmail | Verifique se gerou Senha de Aplicativo e não usou senha comum |
| PyAutoGUI não funciona | Ensure a janela está ativa e com foco |
| WhatsApp não abre | Verifique se Edge está instalado ou altere para Chrome |
| Arquivo `.env` não encontrado | Renomeie `.env.example` para `.env` |


---

## Melhorias Futuras

- Navegar entre múltiplos emails
- Suporte a outros provedores (Outlook, Yahoo, etc.)
- Interface Intuítiva
- Integração com aplicativos mobile
- Agendamento automático (task scheduler)
- Criptografia de credenciais
- Dashboard de estatísticas de emails

---

## Contato

**Carlos Manoel**

-  Email Principal: carlosmanoelrscontato@gmail.com  
-  Email Secundário: carlosmanoeldev@outlook.com
-  GitHub: [carlosmanoelrsdev](https://github.com/carlosmanoelrsdev)



