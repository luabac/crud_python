import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='msn@Root1',
    database='bdyoutube',
)

cursor = conexao.cursor()

#---------CRUD---------


CREATE
nome_produto = "balinha"
valor = 7.5
comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
cursor.execute(comando, (nome_produto, valor))
conexao.commit() # edita o banco de dados


READ
comando = 'SELECT * FROM vendas'
cursor.execute(comando) #cursor é quem executa os comandos SQL dentro dessa conexão
resultado = cursor.fetchall() # ler o banco de dados
for linha in resultado:
    print(linha)

UPDATE
nome_produto = "chocolate"
valor = 15
comando = 'UPDATE vendas SET valor = %s WHERE nome_produto = %s'
cursor.execute(comando, (valor, nome_produto))
conexao.commit() # edita o banco de dados

DELETE
nome_produto = "chocolate"
valor = 9
comando = 'DELETE FROM vendas WHERE nome_produto = %s'
cursor.execute(comando, (nome_produto))
conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()