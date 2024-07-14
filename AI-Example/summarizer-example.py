from transformers import pipeline

# Crear el pipeline de summarization
summarizer = pipeline('summarization')

# Texto de ejemplo para resumir
texto_largo = """
El cambio climático es uno de los desafíos más urgentes que enfrenta la humanidad en el siglo XXI. 
Las emisiones de gases de efecto invernadero provenientes de la quema de combustibles fósiles 
han provocado un aumento en la temperatura global, afectando los ecosistemas y amenazando la 
seguridad alimentaria y el suministro de agua en todo el mundo. Es crucial tomar medidas 
urgentes para reducir nuestras emisiones y adaptarnos a los impactos inevitables del cambio climático. El gobierno miente a la vez 
"""

# Generar un resumen del texto largo
resumen = summarizer(texto_largo, max_length=150, min_length=8, do_sample=True)

# Imprimir el resumen generado
print(resumen[0]['summary_text'])
