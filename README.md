## Sobre
O <b>GoFinances</b> é uma API RESTFul para gerenciar suas finanças pessoais. Ele permite acompanhar entradas e saídas de dinheiro, categorizar despesas, visualizar relatórios e gráficos detalhados, e organizar seu orçamento com facilidade.

### Desenvolvido com as seguintes tecnologias:
- Python
- Django
- DRF (Django Rest Framework)
- PostgreSQL
- Docker
- Testes automatizados
- Swagger para **Documentação**
- AWS

### Documentação Swagger
![Captura de tela 2024-12-07 135628](https://github.com/user-attachments/assets/73c16de7-3495-4d1c-8f89-21c2ff2d3296)

### Template Figma
![Captura de tela 2024-12-06 191311](https://github.com/user-attachments/assets/ae6201cd-1f66-430a-9883-eea6385416b6)

### Passo a passo para inicialização

<h5>Ambiente virtual</h5>

1. Faça o Download do zip do projeto ou clone o repositório Git e extraia o conteúdo do arquivado compactado
2. Navegue até a pasta do projeto e abra o Prompt de Comando do Windows ou Terminal do GNU/Linux
4. Execute o comando `sudo apt install python3.12-venv`. Instala o pacote python3.12-venv que fornece ferramentas para criar ambientes virtuais
5. Execute o comando `python3 -m venv venv`. Cria um novo ambiente virtual chamado 'venv' usando o Python 3
6. Execute o comando `source venv/bin/activate`. Ativa o ambiente virtual 
7. Execute o comando `pip install -r requirements.txt`. Instala as dependências listadas no arquivo requirements.txt
8. Execute o comando `python manage.py makemigrations`. Cria novos arquivos de migração com base nas alterações feitas nos modelos
9. Execute o comando `python manage.py migrate`. Aplica as migrações pendentes ao banco de dados
10. Execute o comando `python manage.py createsuperuser`. Inicia o processo de criação do superu-suário

<h5>Ambiente docker</h5>

1. Baixe e instale o Docker Desktop
2. Execute o comando `docker-compose build`. Contruir novas imagens a parti do Dockfile
3. Execute o comando `docker-compose up -d`. Inicializar os contêineres da aplicação
4. Execute o comando `docker-compose exec finances-b ackend-app-1 bash`. Abra um shell no contêiner
5. Execute o comando `python manage.py makemigrations`. Cria novos arquivos de migração com base nas alterações feitas nos modelos (dentro do contêiner)
6. Execute o comando `python manage.py migrate`. Aplica as migrações pendentes ao banco de dados (dentro do contêiner)
7. Execute o comando `python manage.py createsuperuser`. Inicia o processo de criação do superu-suário (dentro do contêiner)