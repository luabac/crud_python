# CRUD Python com MySQL

Este repositório contém um exemplo simples de aplicação CRUD (Create, Read, Update, Delete) utilizando Python e MySQL. O código demonstra como conectar-se a um banco de dados MySQL, inserir, consultar, atualizar e deletar registros em uma tabela chamada `vendas`.

## Requisitos

- Python 3.x
- Biblioteca `mysql-connector-python`
- MySQL Server

## Instalação

1. Clone este repositório:
	```bash
	git clone https://github.com/seu-usuario/seu-repositorio.git
	```
2. Instale a biblioteca necessária:
	```bash
	pip install mysql-connector-python
	```

## Configuração do Banco de Dados

1. Crie um banco de dados chamado `bdyoutube` no MySQL.
2. Crie a tabela `vendas`:
	```sql
	CREATE TABLE vendas (
		 id INT AUTO_INCREMENT PRIMARY KEY,
		 nome_produto VARCHAR(255),
		 valor FLOAT
	);
	```

## Como usar

O arquivo principal é o `aula.py`, que executa as seguintes operações:

- **CREATE:** Insere um novo produto na tabela.
- **READ:** Lista todos os produtos cadastrados.
- **UPDATE:** Atualiza o valor de um produto existente.
- **DELETE:** Remove um produto da tabela.

Edite as variáveis de conexão no início do arquivo conforme suas credenciais do MySQL.

## Exemplo de execução

```python
import mysql.connector

conexao = mysql.connector.connect(
	 host='localhost',
	 user='root',
	 password='sua_senha',
	 database='bdyoutube',
)
# ... restante do código ...
```

## Licença

Este projeto está sob a licença MIT.
