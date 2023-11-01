from database import Conn
from manager import Manager

trabalho = Manager()

# trabalho.criar_usuario('John', 'teste002')

trabalho.pegar_conexao()
# trabalho.consultar_usuario()
trabalho.consultar_usuario_por_id(11)
# trabalho.atualizar_usuario('Alanis', 'A3090', 6)
# trabalho.deletar_usuario(7)













# ======================================================== #
# print(trabalho.conn_mysql) 
# trabalho.fechar_conexao()
# print(trabalho.conn_mysql) 

      
# Iniciando a classe
# conn = Conn()
# s

# conn.conn_mysql.close()


# INSERT 
# usuarios = [
#     ('Julio', 'biscoito'),
#     ('Andre', '234hnd'),
#     ('Marcello', 'jsaodsda'),
#     ('Fabio', 'jhsadnlsa')
# ]

# for usuario, senha in usuarios:
#     trabalho.pegar_conexao() 
#     trabalho.criar_usuario(usuario, senha)

# REQUIREMENTS
# pip freeze > requirements.txt

# Criando venv: py -m venv venv
# Habilitando venv: . .\venv\Scripts\Activate
# Desativando venv: deactivate