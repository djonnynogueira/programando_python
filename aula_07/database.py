import mysql.connector

# Criando venv: py -m venv venv
# Habilitando venv: . .\venv\Scripts\Activate
# Desativando venv: deactivate

class Conn:
    def __init__(self):
        self.conn_mysql = None
        
    def pegar_conexao(self):
        try:
        
            self.conn_mysql = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'db_usuarios'
            )
            if __name__ == '__main__':
                print("Conexão realizada com sucesso.")
            
        except Exception as e:
            print(e)

if __name__ == '__main__':
    Conn().pegar_conexao()