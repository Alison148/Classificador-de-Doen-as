
# 🌿 Classificador de Natureza com Teorema de Bayes

Este é um projeto em Python com Flask e Scikit-learn que classifica descrições de ambientes naturais como **Floresta**, **Deserto**, **Montanha**, **Praia**, **Lago** ou **Nevado**, utilizando o **Teorema de Bayes (Naive Bayes)** para prever a categoria com base em palavras-chave.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Scikit-learn
- HTML + FontAwesome

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Alison148/-Classificador-de-Natureza---Teorema-de-Bayes.git
cd -Classificador-de-Natureza---Teorema-de-Bayes
(Opcional) Crie um ambiente virtual:

bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash

pip install -r requirements.txt
▶️ Executando o Projeto
bash

python app.py
Acesse o navegador em:

cpp

http://127.0.0.1:5000
💡 Como funciona
Você insere uma descrição do ambiente natural, por exemplo:

"areia, sol forte, cactos e calor"

O sistema utiliza vetorização de texto com CountVectorizer e um modelo Naive Bayes (MultinomialNB) para prever o tipo de natureza, como:

yaml

🏜️ Deserto — Probabilidade: 92%
🧠 Classes Suportadas
🌳 Floresta

🏜️ Deserto

🏔️ Montanha

🏖️ Praia

🌊 Lago

❄️ Nevado

📁 Estrutura do Projeto
pgsql

-Classificador-de-Natureza---Teorema-de-Bayes/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
📃 Licença
Este projeto é open-source e está sob a licença MIT.

👨‍💻 Desenvolvido por
Alison Antunes
github.com/Alison148