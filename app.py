from flask import Flask, render_template,g,request,redirect,jsonify
import sqlite3
import requests
import random

lista = []

# def ligar_banco():
#     banco = g._database = sqlite3.connect('API-Imagens.db')
#     return banco


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', Titulo='API - Robôs')

@app.route('/cadastro')
def cadastro():
    aleatorio = random.randint(1, 283175123912)
    url = f"https://robohash.org/{aleatorio}.png"
    solicitacao = requests.get(url)
    imagem = url
    return render_template('cadastro.html',
                           Titulo='API - Cadastro',
                           imagem=imagem)


# @app.route('/galeria')
# def galeria():
#     banco = ligar_banco()
#     cursor = banco.cursor()
#     cursor.execute('SELECT Descricao, Imagem FROM ImagensAPI')
#     imagens = cursor.fetchall()
#     return render_template('galeria.html', Titulo='API - Galeria', imagensbd = imagens)


@app.route('/galeria')
def galeria():
    return render_template('galeria.html', Titulo='API - Galeria',lista = lista)



@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']
    item = [imagem, descricao]
    lista.append(item)
    return redirect('/cadastro')