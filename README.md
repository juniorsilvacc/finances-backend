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

## Como executar o projeto
<h6>Utilizando ambiente virtual</h6>


1. Faça o Download do zip do projeto ou clone `git clone <URL do repositório>` o repositório Git e extraia o conteúdo do arquivado compactado
2. Navegue até a pasta do projeto e abra o Prompt de Comando do Windows ou Terminal do GNU/Linux
3. Execute o comando `Instala o pacote python3.12-venv`. Fornece ferramentas para criar ambientes virtuais
4. Execute o comando `python3 -m venv venv`. Cria um novo ambiente virtual chamado 'venv' usando o Python 3
5. Execute o comando `source venv/bin/activate`. Ativa o ambiente virtual 
6. Execute o comando `pip install -r requirements.txt`. Instala as dependências listadas no arquivo requirements.txt
7. Execute o comando `python manage.py makemigrations`. Execute as migrações
8. Execute o comando `python manage.py migrate`. Aplique as migrações ao banco de dados
9. Execute o comando `python manage.py createsuperuser`. Inicia o processo de criação do superu-suário

<h5>OBS: Se você estiver usando Docker, os passos 5, 6 e 7 podem ser ignorados, porque o ambiente será configurado dentro do contêiner.</h5>

<h6>Utilizando containers</h6>

1. Baixe e instale o Docker Desktop
2. Execute o comando `docker-compose up --build`. Constrói as imagens Docker necessárias, instala todas as dependências e sobe os serviços
3. Execute o comando `docker exec -it finances-backend-app-1 bash`. Abre o shell com o ambiente do contêiner
4. Execute o comando `python manage.py makemigrations`. Execute as migrações (Dentro do container)
5. Execute o comando `python manage.py migrate`. Aplique as migrações ao banco de dados (Dentro do container)
6. Execute o comando `python manage.py createsuperuser`. Crie um super-usuário (opcional, para acessar o admin do Django)






