# Engenharia de Software II - TP1

## Explicação das tecnologias utilizadas



## Explicação do Sistema

    O Severino App consiste em uma plataforma, onde queremos conectar prestadores de serviço a clientes que precisam de ajuda
    em diversas áreas, atuando como um intermediário entre clientes e prestadores de serviço, simplificando o processo de contratação 
    e garantindo qualidade e confiabiliadade dos serviços prestados.


    O nosso sistema possui algumas funções que o definem, essa que vão ser retradas abaixo: 


    Primeiramente temos a opção de cada usuário ser capaz de realizar um cadastro seu na plataforma, sendo que este cadastro não é separado em um primeiro momento em usuários que prestarão o serviço e usuários que procuram o serviço. Essa opção será um campo do nosso cadastro, fazendo com que se ele for escolhido o usuário será categorizado como 1(cliente) e 2(prestador de serviço)


    Tendo o usuário cadastrado, os usuários que são clientes podem começar a buscaros serviços que desejam, conforme os disponibilizados pela plataforma e os prestadores podem falar quais serviços eles executam. Essa busca pode ser filtrada por cidade, email, usuário, serviço entre outros o que facilita a busca de um usuário ou serviço específico.


    O cliente então, tendo o serviço que ele deseja encontrado, pode então pedir para o prestador o orçamento deste serviço bem como a data para que ele seja executado, ficando a cargo do prestador preencher o preço e o tempo estimado em que ele executará o serviço, além de se ele confima a data. Vale ressaltar que implementaremos também funções para que o cliente consiga acompanhar os serviços que ele já solicitou e o prestador também poderá acompanhar o orçamentos que ele ainda tem que responder e os que já respondeu, assim como um status de cada uma das etapas do processo a partir da solicitação do orçamento.


    Posteriormente, tendo o orçamento sido aceitado pelo prestador ele volta para o cliente para que o mesmo consiga analisar o valor e o tempo de serviço e responda se ele está de acordo ou não com o serviço. Caso seja verdade, o serviço é agendado e executado na data agendada, caso não ele é cancelado.


    Sendo então o serviço marcado para execução, o serviço é executado. Confirmada a execução tanto pelo prestador como pelo cliente. O cliente também fica responsável por avaliar o prestador com uma nota e um comentário.
    

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