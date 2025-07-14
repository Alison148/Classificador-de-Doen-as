from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Dados de treino
descricoes = [
    "muito verde árvores animais rios chuva",            # floresta
    "areia sol calor pouca água cactos seco",            # deserto
    "rochas gelo vento altitude neblina",                # montanha
    "mar areia coqueiros sol surf ondas",                # praia
    "lago árvores calmaria pesca pássaros",              # lago
    "neve frio pinheiros gelo montanha branca",          # neve
]

classes = [
    "Floresta",
    "Deserto",
    "Montanha",
    "Praia",
    "Lago",
    "Nevado"
]

# Treinamento do modelo
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(descricoes)
modelo = MultinomialNB()
modelo.fit(X, classes)

# Função de classificação
def classificar_natureza(texto):
    texto_vetor = vectorizer.transform([texto])
    predicao = modelo.predict(texto_vetor)[0]
    prob = max(modelo.predict_proba(texto_vetor)[0])

    icones = {
        "Floresta": "fa-tree",
        "Deserto": "fa-sun",
        "Montanha": "fa-mountain",
        "Praia": "fa-umbrella-beach",
        "Lago": "fa-water",
        "Nevado": "fa-snowflake"
    }

    return {
        "resultado": predicao,
        "probabilidade": round(prob, 2),
        "icone": f"fa-solid {icones.get(predicao, 'fa-question')}"
    }

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None

    if request.method == 'POST':
        descricao = request.form.get('mensagem', '').strip()
        if not descricao:
            erro = "Descreva o ambiente natural."
        else:
            try:
                resultado = classificar_natureza(descricao)
            except Exception as e:
                erro = f"Erro na análise: {e}"

    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
