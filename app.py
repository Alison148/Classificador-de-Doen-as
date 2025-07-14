from flask import Flask, render_template, request

app = Flask(__name__)

# --- Função aprimorada ---
def classify_symptoms(symptoms_text):
    symptoms_text_lower = symptoms_text.lower()

    if any(term in symptoms_text_lower for term in [
        "câncer", "tumor", "malígno", "quimioterapia", "metástase"
    ]):
        return {
            "resultado": "Grave",
            "probabilidade": 0.95,
            "icone": "fa-solid fa-skull-crossbones"
        }
    elif all(term in symptoms_text_lower for term in [
        "febre alta", "dor no corpo"
    ]) and any(term in symptoms_text_lower for term in [
        "tosse seca", "dificuldade para respirar"
    ]):
        return {
            "resultado": "Grave",
            "probabilidade": 0.85,
            "icone": "fa-solid fa-virus"
        }
    elif any(term in symptoms_text_lower for term in [
        "dor no peito", "falta de ar", "dificuldade para respirar", "formigamento no braço",
        "paralisia", "fala arrastada", "perda de consciência", "confusão mental",
        "convulsão", "rigidez na nuca", "visão turva", "desmaio", "batimentos irregulares",
        "pele arroxeada", "lábios roxos", "hemorragia", "sangramento intenso",
        "suor frio", "abdômen rígido", "dor abdominal extrema"
    ]):
        return {
            "resultado": "Grave",
            "probabilidade": 0.90,
            "icone": "fa-solid fa-triangle-exclamation"
        }
    elif any(term in symptoms_text_lower for term in [
        "febre", "dor de cabeça", "gripe", "resfriado", "congestão nasal", "espirro"
    ]):
        return {
            "resultado": "Leve",
            "probabilidade": 0.70,
            "icone": "fa-solid fa-thermometer-half"
        }
    elif any(term in symptoms_text_lower for term in [
        "dor de barriga", "enjoo", "diarreia", "náusea", "vômito"
    ]):
        return {
            "resultado": "Leve",
            "probabilidade": 0.65,
            "icone": "fa-solid fa-poo"
        }
    elif any(term in symptoms_text_lower for term in [
        "sem sintomas", "saudável", "tudo bem", "me sinto bem"
    ]):
        return {
            "resultado": "Benigna",
            "probabilidade": 0.99,
            "icone": "fa-solid fa-heart-pulse"
        }
    else:
        return {
            "resultado": "Indefinido",
            "probabilidade": 0.40,
            "icone": "fa-solid fa-question"
        }

# --- Rota principal ---
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_final = None
    erro = None

    if request.method == 'POST':
        symptoms = request.form['mensagem']
        if not symptoms:
            erro = "Por favor, descreva os sintomas para análise."
        else:
            try:
                resultado_final = classify_symptoms(symptoms)
            except Exception as e:
                erro = f"Ocorreu um erro na análise: {e}"

    return render_template('index.html', resultado_final=resultado_final, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
