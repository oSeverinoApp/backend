# Engenharia de Software II - TP1

## Integrantes:

- Bernardo Franco Tormin
- Felipe da Cruz Basilio
- Gustavo Ribeiro Alves Rodrigues
- Raphael Pedra Paulucci
- Tainan Henrique de Albuquerque

## Ferramentas necessárias:

- PostgreSQL versão 12.18 ou superior;
- Docker-compose 1.25.0 ou superior;
- Python3.10.14;

## Ativação da docker

- Passos (Ubuntu):

1. `sudo apt update`
2. `sudo apt install postgresql postgresql-contrib`
3. `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
4. `sudo chmod +x /usr/local/bin/docker-compose`
5. `sudo apt install docker.io`
6. `sudo systemctl start docker`
7. `sudo systemctl enable docker`
8. `sudo usermod -aG docker $USER`
9. `newgrp docker`

- Depois de realizar os passos indicados, utilizar o comando `docker-compose up -d` dentro do diretório do **backend** para ativar a docker para o serviço do postgreSQL e posterior geração e uso do banco de dados para queries.

- Conferir via comando `psql -h localhost -p 5433 -U severinoapp -d severinoapp_db` se ocorre o acesso ao banco de dados do postgreSQL corretamente.

## Setup

- Utilizar o comando `pip install -r nrequirements.txt` no diretório **backend** para instalar as dependências necessárias para executar a aplicação.

## Rodar aplicação:

- `cd src`
- `python3 app.py` ou `python app.py`

## Popular o DB
- Para popular o banco de dados basta clicar no link abaixo
http://127.0.0.1:5000/api/populate_db

ou

http://localhost:5000/api/pupolate_db


## Sempre que alterar o infraestructure models, deve ser pagado todas as tabelas do dB, ao rodar o comandp python3 app.py, o banco de dados é recriado e deve-se acessar algum dos links acima para repopula-lo

## Para apagar as tabelas basta acessar
http://127.0.0.1:5000/api/drop_db

ou

http://localhost:5000/api/drop_db

## TESTES

Para a execução dos testes, execute os comandos abaixo:

**docker-compose -f docker-compose.test.yml up -d**

Para inicializar o banco de testes use o comando:

**python init_test_db.py**

Verifique se foi criado corretamente a partir do comando:

**psql -h localhost -p 5434 -U severinoapp_test -d severinoapp_test_db**


