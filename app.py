from flask import (Flask, request)

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    nome = request.args.get('nome')
    return f"""<h1>Página Inicial</h1> 
    <P>Olá {nome}, que nome bonito!</P>
    """

@app.route("/galeria", methods =('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods =('GET',))
def contato():
    return "<h1>Contato</h1>"

@app.route("/Sobre", methods =('GET',))
def sobre():
    return "<h1>Sobre</h1>"