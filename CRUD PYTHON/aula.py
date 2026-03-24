import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='msn@Root1',
    database='bdyoutube',
)

cursor = conexao.cursor()

#---------CRUD---------


# CREATE
# nome_produto = "balinha"
# valor = 7.5
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando) #cursor é quem executa os comandos SQL dentro dessa conexão
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

# UPDATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
nome_produto = "chocolate"
valor = 9
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()





# import mysql.connector

# conexao = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='msn@Root1',
#     database=''
# )

# cursor = conexao.cursor()

# nome_produto = ""
# valor = ""
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", valor)'
# cursor.execute(comando)
# conexao.commit()



# comando
# cursor.execute(comando)
# conexao.commit()