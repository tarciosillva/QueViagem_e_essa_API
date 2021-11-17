from werkzeug.wrappers import request
import mysql.connector
from logging import debug
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

cnx = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='queviagemeessa?'
)
cursor = cnx.cursor()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/buyTickets', methods=['POST'])
def buyTickets():
    data = request.get_json()

    opcao = data['opcao']
    origem = data['origem']
    destino = data['destino']
    data_ida = data['data_ida'],
    data_volta = data['data_volta'],
    numeroTotal = data['numero'],
    idade = data['idade']

    nome_cartao = data['nome_cartao'],
    numero_cartao = data['numero_cartao'],
    validade = data['validade'],
    numero_parcelas = data['numero_parcelas'],
    valor_parcelas = data['valor_parcelas'],
    total = data['total'],
    tipoCompra = data['tipoCompra']

    cursor.execute(
        "INSERT INTO passagens (opcao, origem, destino, data_ida, data_volta, idade, numeroTotal) VALUES (%s, %s, %s, %s, %s, %s, %s);", (opcao, origem, destino, data_ida[0], data_volta[0], idade, numeroTotal[0]))

    cursor.execute(
        "INSERT INTO compra (nome_cartao, numero_cartao, validade, numero_parcelas, valor_parcelas, total, tipoCompra) VALUES (%s, %s, %s, %s, %s, %s, %s);", (nome_cartao[0], numero_cartao[0], validade[0], numero_parcelas[0], valor_parcelas[0], total[0], tipoCompra))

    cnx.commit()

    return jsonify(data)


@app.route('/queryTickets', methods=['GET'])
def queryTickets():
    cursor.execute("SELECT * FROM passagens")
    results = cursor.fetchall()
    payload = []
    content = {}

    for result in results:
        content = {'opcao': result[1], 'origem': result[2], 'destino': result[3], 'data_ida': result[4],'data_volta': result[5],'numero': result[7],'idade': result[6]}
        payload.append(content)
        content = {}
    return jsonify(payload)


@app.route('/buyAccommodation', methods=['POST'])
def buyAccommodationickets():
    data = request.get_json()

    destino = data['destino']
    data_entrada = data['data_entrada']
    data_saida = data['data_saida']
    numero_quartos = data['numero_quartos'],
    numeroPessoas = data['numeroPessoas'],
    idade = data['idade'],

    nome_cartao = data['nome_cartao'],
    numero_cartao = data['numero_cartao'],
    validade = data['validade'],
    numero_parcelas = data['numero_parcelas'],
    valor_parcelas = data['valor_parcelas'],
    total = data['total'],
    tipoCompra = data['tipoCompra']

    cursor.execute(
        "INSERT INTO hospedagem (destino, data_entrada, data_saida, numero_quartos, numeroPessoas, idades) VALUES (%s, %s, %s, %s, %s, %s);", (destino, data_entrada, data_saida, numero_quartos[0], numeroPessoas[0], idade[0]))

    cursor.execute(
        "INSERT INTO compra (nome_cartao, numero_cartao, validade, numero_parcelas, valor_parcelas, total, tipoCompra) VALUES (%s, %s, %s, %s, %s, %s, %s);", (nome_cartao[0], numero_cartao[0], validade[0], numero_parcelas[0], valor_parcelas[0], total[0], tipoCompra))

    cnx.commit()

    return jsonify(data)


@app.route('/queryAccommodation', methods=['GET'])
def queryAccommodationickets():
    cursor.execute("SELECT * FROM hospedagem")
    results = cursor.fetchall()
    payload = []
    content = {}

    for result in results:
        content = {'destino': result[1], 'data_entrada': result[2], 'data_saida': result[3], 'numero_quartos': result[4],'numeroPessoas': result[5],'idades': result[6]}
        payload.append(content)
        content = {}
    return jsonify(payload)

   
