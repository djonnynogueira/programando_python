# REQUIREMENTS
# pip freeze > requirements.txt

# Criando venv: py -m venv venv
# Habilitando venv: . .\venv\Scripts\Activate
# Desativando venv: deactivate

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

    # sql = 'INSERT INTO tb_funcionarios (Nome, idade, cargo, salario, irpf) VALUES (%s, %s, %s, %s, %s)'

    cursor = conn_mysql.cursor()
    
    cursor.execute("SELECT * FROM tb_funcionarios")
    
    select = cursor.fetchall()
    
    for x in select:
        print(x)
    
    conn_mysql.commit()

    conn_mysql.close()    
   
    print("Select gerado com sucesso!")
       
except Exception as e:
    print(e)
    
