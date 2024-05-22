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
-- sudo apt update
-- sudo apt install postgresql postgresql-contrib
-- sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
-- sudo chmod +x /usr/local/bin/docker-compose
-- sudo apt install docker.io
-- sudo systemctl start docker
-- sudo systemctl enable docker
-- sudo usermod -aG docker $USER
-- newgrp docker

- Depois de realizar os passos indicados, utilizar o comando **docker-compose up -d** dentro do diretório do **backend** para ativar a docker para o serviço do postgreSQL e posterior geração e uso do banco de dados para queries.

- Conferir via comando **psql -h localhost -p 5433 -U severinoapp -d severinoapp_db** se ocorre o acesso ao banco de dados do postgreSQL corretamente.


