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

@app.route("/calculo_juros", methods=('GET', 'POST'))
def calculo_juros():
    if request.method == 'POST':
        investimento = float(request.form['investimento'])
        juros_anuais = float(request.form['juros']) / 100
        tempo_meses = int(request.form['tempo'])
        contribuicao = float(request.form['contribuicao'])

        montante = investimento
        for mes in range(tempo_meses):
            montante += contribuicao
            montante *= (1 + juros_anuais / 12)

        return f'Valor final após {tempo_meses} meses: R$ {montante:.2f}'

    return render_template('calculo_juros.html')


@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if email == 'aluno@senai.br' and senha == 'senai':
            return '<h1>Usuário Logado com Sucesso!</h1>'
        else:
            return '<h1>Usuário ou senha incorretos. Tente novamente.</h1>'

    return render_template('login.html')

@app.route("/imc", methods=('GET', 'POST'))
def calcular_imc():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = 'Magreza'
                grau_obesidade = 0
            elif 18.5 <= imc <= 24.9:
                classificacao = 'Normal'
                grau_obesidade = 0
            elif 25.0 <= imc <= 29.9:
                classificacao = 'Sobrepeso'
                grau_obesidade = 1
            elif 30.0 <= imc <= 39.9:
                classificacao = 'Obesidade'
                grau_obesidade = 2
            else:
                classificacao = 'Obesidade Grave'
                grau_obesidade = 3

            return f'''
                <h1>Seu IMC é: {imc:.2f}</h1>
                <h2>Classificação: {classificacao}</h2>
                <h2>Grau de Obesidade: {grau_obesidade}</h2>
            '''
        except ValueError:
            return '<h1>Erro: Por favor insira valores válidos para peso e altura.</h1>'
    
    return render_template('imc.html')
