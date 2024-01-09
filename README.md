# Python Scripts Repository 🐍

Bem-vindo ao repositório de scripts Python úteis! Aqui você encontrará uma coleção de scripts para facilitar tarefas comuns e melhorar sua produtividade.

## Como Configurar o Ambiente de Desenvolvimento Python 3.11

### Windows 💻

1. **Baixar o Python 3.11:**
   - Acesse [python.org](https://www.python.org/downloads/) e baixe a versão mais recente do Python 3.11 para Windows.
   - Durante a instalação, marque a opção "Adicionar Python 3.x ao PATH" para facilitar o acesso ao Python pelo terminal.

2. **Instalar um Ambiente Virtual (opcional, mas recomendado):**
   - Abra o terminal e navegue até o diretório do seu projeto.
   - Execute o comando:
     ```bash
     python -m venv venv
     ```

3. **Ativar o Ambiente Virtual:**
   - No terminal, dentro do diretório do projeto, execute:
     - PowerShell:
       ```powershell
       .\venv\Scripts\Activate
       ```
     - CMD:
       ```cmd
       .\venv\Scripts\activate.bat
       ```

4. **Instalar Dependências:**
   - Com o ambiente virtual ativado, instale as dependências do seu projeto usando o pip:
     ```bash
     pip install -r requirements.txt
     ```

5. **Pronto!**
   - Seu ambiente de desenvolvimento Python 3.11 no Windows está configurado. Comece a utilizar os scripts!

### Linux 🐧

1. **Instalar o Python 3.11:**
   - Utilize o gerenciador de pacotes da sua distribuição Linux para instalar o Python 3.11.
     ```bash
     sudo apt-get update
     sudo apt-get install python3.11
     ```

2. **Instalar o pip:**
   - Instale o pip, o gerenciador de pacotes do Python:
     ```bash
     sudo apt-get install python3.11-venv python3.11-dev python3-pip
     ```

3. **Instalar um Ambiente Virtual (opcional, mas recomendado):**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     python3.11 -m venv venv
     ```

4. **Ativar o Ambiente Virtual:**
   - No terminal, dentro do diretório do projeto, execute:
     ```bash
     source venv/bin/activate
     ```

5. **Instalar Dependências:**
   - Com o ambiente virtual ativado, instale as dependências do seu projeto usando o pip:
     ```bash
     pip install -r requirements.txt
     ```

6. **Pronto!**
   - Seu ambiente de desenvolvimento Python 3.11 no Linux está configurado. Comece a utilizar os scripts!

## Scripts Disponíveis

- [request_girhub_status.py: Busca o status do Github e cria um arquivo de registro.](./request_girhub_status.py)
- [check_domain_availability.py: Verifica a disponibilidade de um dominio utilizando o serviço WhoIs](./check_domain_availability.py)
- [organize_files.py: organiza os documentos pela extenção](./organize_files.py)

Sinta-se à vontade para contribuir ou sugerir melhorias! 😊