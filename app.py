from flask import (Flask, render_template, request) 

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    nome = request.args.get('nome')
    return f"""<h1>Página inicial</h1> <p>Eu sou a Manu</p>
        <p>Olá {nome}, que nome bonito!
    """
@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato (17) 99111-2323</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre...</h1>"

@app.route("/area")
def area():
  altura = float (request.args.get('a'))
  largura = float(request.args.get('l'))
  return f""" 
<h1> A área informada> L={largura}* A={altura} Area={largura*altura}</h1>"""

@app.route("/parimpar", methods=('GET',))
def parimpar():
  numero = float(request.args.get('n'))
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/nomesob", methods=('GET',))
def nomesob():
  nome = request.args.get('nome')
  sobrenome = request.args.get('sobrenome')
  return f"""<h1> Sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero=None): #None desobriga o valor
  if 'numero' in request.args:
     numero= int(request.args.get('numero'))
  
  return render_template('tabuada.html',numero=numero)


