import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Inicializar o analisador de sentimentos
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analisar_sentimento(texto):
    sentimento = sia.polarity_scores(texto)

    if sentimento['compound'] > 0.05:
        return "Positivo 😊"
    elif sentimento['compound'] < -0.05:
        return "Negativo 😞"
    else:
        return "Neutro 😐"

# Testando o programa
texto = input("Digite um texto para análise de sentimento: ")
resultado = analisar_sentimento(texto)
print(f"Sentimento detectado: {resultado}")

