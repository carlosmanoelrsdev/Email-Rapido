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
Email-Rápido/
├── App.py                    # Ponto de entrada da aplicação
├── config.py                 # Carregamento de variáveis de ambiente
├── configJSON.py             # Funções de leitura do JSON de emails
├── ConfigEmails.py           # Lógica principal de conexão e leitura de emails
├── EnvioWhatsapp.py          # Automação de envio via WhatsApp Web
├── emails.json               # Múltiplas contas de email (não incluído no git)
├── emailsExample.json        # Exemplo de configuração de emails
├── email.txt                 # Arquivo de backup com emails (não incluído no git)
├── .env                      # Variáveis de ambiente (não incluído no git) Descontinuado
├── .env.example              # Exemplo de variáveis de ambiente. Descontinuado
├── .gitignore                # Arquivos ignorados pelo git
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

---

## Alterações Recentes

### Versão 2.0 - Suporte a Múltiplas Contas

✅ **Adicionado:**
- Suporte para múltiplas contas de Gmail no `emails.json`
- Menu de seleção de conta ao iniciar a aplicação
- Melhor organização das credenciais
- Correção do bug de comparação de tipos na validação de entrada

✅ **Melhorado:**
- UX: Interface mais intuitiva para escolher a conta
- Código mais robusto e tratamento de erros

⚠️ **Descontinuado:**
- Configuração via `.env` - Use `emails.json` em seu lugar
- `.env.example` foi movido para `emailsExample.json`

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
git clone https://github.com/carlosmanoelrsdev/Email-Rapido.git
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

#### 4. Configure Múltiplas Contas de Email (NOVO)

A partir desta atualização, você pode configurar **múltiplas contas de Gmail** usando o arquivo `emails.json`:

**Copie `emailsExample.json` para `emails.json`:**

```bash
# Windows
copy emailsExample.json emails.json

# Linux/Mac
cp emailsExample.json emails.json
```

**Estrutura do `emails.json`:**

```json
{
    "emails": [
        {
            "ID": 0,
            "servidor": "imap.gmail.com",
            "email": "primeira.conta@gmail.com",
            "senhaAPP": "sua senha de app aqui"
        },
        {
            "ID": 1,
            "servidor": "imap.gmail.com",
            "email": "segunda.conta@gmail.com",
            "senhaAPP": "sua senha de app aqui"
        }
    ]
}
```

**Como usar:**

1. Execute o programa: `python App.py`
2. O programa mostrará todas as contas configuradas
3. Digite o **ID** da conta que deseja usar
4. Os emails serão capturados e salvos

**⚠️ IMPORTANTE - Segurança:**
- O arquivo `emails.json` está no `.gitignore` e **NÃO será commitado**
- Nunca compartilhe ou publique seu arquivo `emails.json` com credenciais reais
- Use apenas **Senhas de Aplicativo** do Gmail (não a senha principal)

#### 6. Obtenha a Senha de Aplicativo Gmail

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
5
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
| **config.py** | Carregamento de credenciais (Descontinuado) |
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
| Arquivo `emails.json` não encontrado | Copie `emailsExample.json` para `emails.json` e configure suas contas |


---

## Melhorias Futuras

- ✅ ~~Navegar entre múltiplos emails~~ (Adicionado na v2.0)
- Suporte a outros provedores (Outlook, Yahoo, etc.)
- Interface Gráfica Intuitiva
- Integração com aplicativos mobile
- Agendamento automático (task scheduler)
- Criptografia de credenciais locais
- Dashboard de estatísticas de emails
- API REST para integração externa

---

## Contato

**Carlos Manoel**

- Email Principal: carlosmanoelrscontato@gmail.com
- Email Secundário: carlosmanoeldev@outlook.com
- GitHub: [carlosmanoelrsdev](https://github.com/carlosmanoelrsdev)




