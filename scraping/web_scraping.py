from bs4 import BeautifulSoup

import requests

#Recebendo conteudo da requisição http do site
site = requests.get('https://climatempo.com.br/').content
#Baixando o html do site
soup = BeautifulSoup(site, 'html.parser')

#Transforma o html em string
#print(soup.prettify())

#temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

#print(temperatura)

print(soup.title.string)
print(soup.p.string)
print(soup.find('admin'))