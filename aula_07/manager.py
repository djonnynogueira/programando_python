from database import Conn

class Manager(Conn):
    def fechar_conexao(self):
        self.conn_mysql.close()
     
     # CRUD: [C]RUD   
    def criar_usuario(self, nome, senha):
        #query
        sql = 'INSERT INTO tb_usuarios(usuario, senha) VALUES (%s, %s)'
        
        #cursos para oprerações
        cursor = self.conn_mysql.cursor()
        
        #Executando as operações
        cursor.execute(sql, [nome, senha])
        self.conn_mysql.commit()
        
        self.conn_mysql.close()
        
        print('Usuario inserido com sucesso!')
    
     # CRUD: C[R]UD     
    def consultar_usuario(self):
        #query
        sql = "SELECT usuario, senha FROM tb_usuarios"
        
        # Definir a variável cursor como um objeto de conexão com o banco de dados     
        cursor = self.conn_mysql.cursor()
        # Executar a consulta usando o método execute() do objeto cursor
        cursor.execute(sql)
        
        # for registro in cursor:
        #     print(registro)
        
        # Iterar sobre os resultados da consulta e imprimir cada linha
        for usuario, senha in cursor:
            print(f"Usuario: {usuario}, senha: {senha}")
        
        # select = cursor.fetchall()
        # for x in select:
        # print(x)
        self.conn_mysql.close()
     # CRUD: CR[U]D 
    def atualizar_usuario(self, nome, senha, id):
        sql = "UPDATE tb_usuarios SET usuario=%s, senha=%s WHERE id=%s"
         
        cursor = self.conn_mysql.cursor()
         
        cursor.execute(sql, [nome, senha, id])
         
        self.conn_mysql.commit()        
        
        print(f'Foram alterados {cursor.rowcount} registro(s)!')
    
        self.conn_mysql.close()
        
     # CRUD: CRU[D]   
    def deletar_usuario(self, id):
        sql = "DELETE FROM tb_usuarios WHERE id=%s"
         
        cursor = self.conn_mysql.cursor()
         
        cursor.execute(sql, [id])
         
        self.conn_mysql.commit()        
        
        print(f'Foram deletados {cursor.rowcount} registro(s)!')
         
        self.conn_mysql.close()
     # CRUD: C[R]UD        
    def consultar_usuario_por_id(self, id):
        #query
        sql = "SELECT id, usuario, senha FROM tb_usuarios WHERE id=%s"
        
        # Definir a variável cursor como um objeto de conexão com o banco de dados     
        cursor = self.conn_mysql.cursor()
        # Executar a consulta usando o método execute() do objeto cursor
        cursor.execute(sql, [id])

        # Iterar sobre os resultados da consulta e imprimir cada linha
        for id, usuario, senha in cursor:
            print(f"Id: {id}, Usuario: {usuario}, senha: {senha}")
        
        self.conn_mysql.close()

    
  