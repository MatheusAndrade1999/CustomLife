from flask import Flask, render_template, request, url_for, jsonify
# from flask_mysqldb import MySQL

#Banco de dados
# app.config['MYSQL_Host'] = 'localhost' #127.0.0.1
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '1234'
# app.config['MYSQL_DB'] = 'contato'

# mysql = MySQL(app)

app = Flask("__name__")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suzuki')
def suzuki():
    return render_template('suzuki.html')

# @app.route('/contato')
# def contato():
#     return render_template('contato.html')

# @app.route('/contato', methods=['GET', 'POST'])
# def contato():
#     if request.method == "POST":
#         email = request.form['email']
#         assunto = request.form['assunto']
#         descricao = request.form['descricao']

#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO contatos(email, assunto, descricao), VALUES (%s, %s, %s)", (email, assunto, descricao))
        
#         mysql.connection.commit()

#         cur.close()

#         return 'sucesso'
#     return render_template('contato.html')

#rota usuarios para listar todos os usuarios do banco de dados
# @app.route('/users')
# # def users():
# #     # cur = mysql.connection.cursor()