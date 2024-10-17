from flask import (Flask, request)

app = Flask(__name__)

@app.route("/sting:nome", methods=('GET',))
def index():
    return "<h1>Página Inicial</h1>"

@app.route("/area/<float:altura>/<float:largura>" , methods=("GET",))
def area(largura, altura):
    
    return f"""<h1> A área informada> L={largura}* A={altura} => Area={largura*altura} <h1>"""

@app.route("/parimpar/<float:numero>", methods=('GET',))
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

@app.route("/potencia/<float:numero>/<float:elevado>", methods=('GET',))
def potencia(numero: float, elevado: float):
    return f"""<h1>A potencia é> N={numero}* E={elevado} => Potencia={numero*elevado}</h1>"""



