from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask("__name__")

mysql = MySQL(app)
#Banco de dados
app.config['MYSQL_Host'] = 'localhost' #127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'contato'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suzuki')
def suzuki():
    return render_template('suzuki.html')

@app.route('/honda')
def honda():
    return render_template('honda.html')

@app.route('/yamaha')
def yamaha():
    return render_template('yamaha.html')

@app.route('/retorno')
def retorno():
    return render_template('/retorno')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        
        mysql.connection.commit()

        cur.close()

       
    return render_template('retorno.html')

@app.route('/users')
def users():
	cur = mysql.connection.cursor()

	users = cur.execute("SELECT * FROM contato")

	if  users > 0:
		userDetails = cur.fetchall()
		
		return render_template("users.html", userDetails=userDetails)

# rota usuarios para listar todos os usuarios do banco de dados
# @app.route('/users')
# def users():
#     # cur = mysql.connection.cursor()