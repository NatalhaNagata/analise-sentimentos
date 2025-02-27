# Analisador de Sentimentos 🤖

Este é um simples **Analisador de Sentimentos** usando Python e a biblioteca NLTK. Ele recebe um texto como entrada e classifica o sentimento como **Positivo**, **Negativo** ou **Neutro**.

## 📌 Como funciona?
1. O programa pede um texto ao usuário.
2. Ele analisa o sentimento usando `SentimentIntensityAnalyzer` do `NLTK`.
3. Retorna se o texto tem um **sentimento positivo, negativo ou neutro**.

## 🚀 Como rodar o projeto?
### 1️⃣ Instale os requisitos:
```bash
pip install nltk
python -m nltk.downloader vader_lexicon
