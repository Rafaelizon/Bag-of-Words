# Rafael Guaitanele Niszczak

import requests
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

sentencas = []
texto = " "
texto2 = ""

paginas = [
  "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",
  "https://hbr.org/2022/04/the-power-of-natural-language-processing",
  "https://en.wikipedia.org/wiki/Natural_language_processing",
  "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html",
  "https://monkeylearn.com/natural-language-processing/"
]

for site in paginas:
  pagina = requests.get(site)
  soup = BeautifulSoup(pagina.content, 'html.parser')
  contador = 0

  while contador < 100:
    try:
      string = (soup.find_all('title')[contador].get_text())
      string = string.split(" ")
      sentencas.append(string)
    except:
      exception = "isso só faz o try/except parar e voltar para o loop."
    contador = contador + 1
    try:
      string = (soup.find_all('p')[contador].get_text())
      string = string.split(" ")
      sentencas.append(string)
    except:
      exception = "isso só faz o try/except parar e voltar para o loop."

x = 0
while x < len(sentencas):

  texto = sentencas[x]
  texto3 = FreqDist(texto)
  print(texto3.most_common())
  x = x + 1
