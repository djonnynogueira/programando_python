import mysql.connector


try:
    conn_mysql = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'db_funcionarios'
    )
    
    print("Conexão realizada com sucesso!")
    
    # sql_cons = 'select * from tb_funcionarios'

    sql = 'INSERT INTO tb_funcionarios (Nome, idade, cargo, salario, irpf) VALUES (%s, %s, %s, %s, %s)'

    cursor = conn_mysql.cursor()
    
    cursor.execute(sql, ['Jose', 18, 'Professor', 5000, 600])
    conn_mysql.commit()

    conn_mysql.close()
    
    print("Inserido com sucesso!")
    
except Exception as e:
    print(e)
    
