# Engenharia de Software II - TP1

## Explicação das tecnologias utilizadas

## Explicação do Sistema

- O Severino App consiste em uma plataforma onde queremos conectar prestadores de serviço a clientes que precisam de ajuda em diversas áreas, atuando como um intermediário entre clientes e prestadores de serviço, simplificando o processo de contratação e garantindo a qualidade e a confiabilidade dos serviços prestados.

O nosso sistema possui algumas funções que o definem, as quais serão retratadas abaixo:

- Primeiramente, temos a opção de cada usuário realizar um cadastro na plataforma, sendo que este cadastro não é separado, em um primeiro momento, em usuários que prestarão o serviço e usuários que procurarão o serviço. Essa opção será um campo do nosso cadastro, fazendo com que, se for escolhido, o usuário será categorizado como 1 (cliente) e 2 (prestador de serviço).

- Com o usuário cadastrado, os usuários que são clientes podem começar a buscar os serviços que desejam, conforme os disponibilizados pela plataforma, e os prestadores podem informar quais serviços eles executam. Essa busca pode ser filtrada por cidade, e-mail, usuário, serviço, entre outros, o que facilita a busca de um usuário ou serviço específico.

- O cliente, tendo encontrado o serviço que deseja, pode pedir ao prestador o orçamento deste serviço, bem como a data para que ele seja executado, ficando a cargo do prestador preencher o preço e o tempo estimado em que executará o serviço, além de confirmar a data. Vale ressaltar que implementaremos também funções para que o cliente consiga acompanhar os serviços que já solicitou e o prestador possa acompanhar os orçamentos que ainda tem que responder e os que já respondeu, assim como um status de cada uma das etapas do processo a partir da solicitação do orçamento.

- Posteriormente, tendo o orçamento sido aceito pelo prestador, ele volta para o cliente para que este consiga analisar o valor e o tempo de serviço e responda se está de acordo ou não com o serviço. Caso esteja, o serviço é agendado e executado na data marcada; caso contrário, ele é cancelado.

- Sendo o serviço marcado para execução, ele é executado. A execução é confirmada tanto pelo prestador quanto pelo cliente. O cliente também é responsável por avaliar o prestador com uma nota e um comentário.

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

### Passos (Ubuntu):

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

## Sempre que alterar o infraestructure models, deve ser apagado todas as tabelas do dB, ao rodar o comando python3 app.py, o banco de dados é recriado e deve-se acessar algum dos links acima para repopula-lo

## Para apagar as tabelas basta acessar

http://127.0.0.1:5000/api/drop_db

ou

http://localhost:5000/api/drop_db

## TESTES

Para a execução dos testes, execute os comandos abaixo:

**docker-compose -f docker-compose.test.yml up -d**

Para inicializar o banco de testes use o comando:

**python init_test_db.py**

ou

**python3 init_test_db.py**

Verifique se foi criado corretamente a partir do comando:

**psql -h localhost -p 5434 -U severinoapp_test -d severinoapp_test_db**
