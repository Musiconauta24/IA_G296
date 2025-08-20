from transformers import pipeline

# OJO: usar 'sentiment-analysis'
clasificador = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment")

# Analizar una sentencia
resultado = clasificador([
    "Me encantaría usar la librería de transformers de python",
])
print(resultado)
resultado = clasificador([
    "Estoy muy triste"
])
print(resultado)
