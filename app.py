from flask import Flask, render_template, request

app = Flask(__name__)

# --- Placeholder for a simplified "model" ---
# In a real application, you'd load a pre-trained ML model here.
# For demonstration, we'll use a simple keyword-based classification.

def classify_symptoms(symptoms_text):
    """
    A placeholder function to classify symptoms.
    In a real app, this would be a sophisticated ML model.
    """
    symptoms_text_lower = symptoms_text.lower()

    if "câncer" in symptoms_text_lower or \
       "tumor" in symptoms_text_lower or \
       "malígno" in symptoms_text_lower or \
       "quimioterapia" in symptoms_text_lower or \
       "metástase" in symptoms_text_lower:
        return {
            "resultado": "Grave",
            "probabilidade": 0.95, # High confidence for demonstration
            "icone": "fa-solid fa-skull-crossbones"
        }
    elif "febre alta" in symptoms_text_lower and \
         ("tosse seca" in symptoms_text_lower or "dificuldade para respirar" in symptoms_text_lower) and \
         "dor no corpo" in symptoms_text_lower:
        return {
            "resultado": "Grave",
            "probabilidade": 0.85,
            "icone": "fa-solid fa-virus"
        }
    elif "febre" in symptoms_text_lower or \
         "dor de cabeça" in symptoms_text_lower or \
         "gripe" in symptoms_text_lower or \
         "resfriado" in symptoms_text_lower or \
         "congestão nasal" in symptoms_text_lower:
        return {
            "resultado": "Leve",
            "probabilidade": 0.70,
            "icone": "fa-solid fa-thermometer-half"
        }
    elif "dor de barriga" in symptoms_text_lower or \
         "enjoo" in symptoms_text_lower or \
         "diarreia" in symptoms_text_lower:
        return {
            "resultado": "Leve",
            "probabilidade": 0.65,
            "icone": "fa-solid fa-poo" # Just for fun, you might want a more medical icon
        }
    elif "sem sintomas" in symptoms_text_lower or \
         "saudável" in symptoms_text_lower or \
         "tudo bem" in symptoms_text_lower:
        return {
            "resultado": "Benigna",
            "probabilidade": 0.99,
            "icone": "fa-solid fa-heart-pulse"
        }
    else:
        # Default for unrecognized patterns
        return {
            "resultado": "Leve", # Default to 'Leve' if nothing specific matches
            "probabilidade": 0.50,
            "icone": "fa-solid fa-question"
        }

# --- Flask Routes ---
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
                # Call our placeholder classification function
                classification_output = classify_symptoms(symptoms)
                resultado_final = classification_output
            except Exception as e:
                erro = f"Ocorreu um erro na análise: {e}"

    return render_template('index.html', resultado_final=resultado_final, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)