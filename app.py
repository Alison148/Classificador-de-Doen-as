from flask import Flask, render_template, request

app = Flask(__name__)

# Probabilidades baseadas em um exemplo simples
prob_spam = 0.4
prob_nao_spam = 0.6
palavras_spam = {'ganhe': 0.7, 'dinheiro': 0.6, 'agora': 0.5}
palavras_nao_spam = {'ganhe': 0.1, 'dinheiro': 0.2, 'agora': 0.1}

def calcular_probabilidade_bayes(mensagem):
    palavras = mensagem.lower().split()
    p_spam = prob_spam
    p_nao_spam = prob_nao_spam
    for palavra in palavras:
        p_spam *= palavras_spam.get(palavra, 0.01)
        p_nao_spam *= palavras_nao_spam.get(palavra, 0.01)
    return "Spam" if p_spam > p_nao_spam else "Não Spam"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        resultado = calcular_probabilidade_bayes(mensagem)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
