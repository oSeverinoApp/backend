import psycopg2

# Dados de conexão
HOST = "localhost"
PORT = "5432"
USER = "severinoapp_test"
PASSWORD = "severinoapp_test"
DB_NAME = "severinoapp_test_db"

# Função para executar os comandos SQL do arquivo .sql
def execute_sql_file(filename, connection):
    # Abrir o arquivo .sql
    with open(filename, 'r') as file:
        # Ler e dividir os comandos SQL
        sql_commands = file.read().split(';')

        # Para cada comando SQL
        for command in sql_commands:
            # Remover espaços em branco e quebras de linha extras
            command = command.strip()
            if command:
                # Executar o comando SQL
                cursor = connection.cursor()
                cursor.execute(command)
                cursor.close()

# Conectar ao banco de dados
try:
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    print("Conexão bem-sucedida!")

    # Executar os comandos SQL do arquivo .sql
    execute_sql_file("init_test_db.sql", conn)

    # Commit das alterações
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    # Fechar a conexão
    if conn is not None:
        conn.close()