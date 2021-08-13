import requests
#Trabalhar com xml e html
from bs4 import BeautifulSoup
import operator
#Manipulacao de listas, tuplas, dicionario
from collections import Counter


def start(url):
    #Armazenar conteudo do site passado
    wordlist = []
    source_code = requests.get(url).text

    #Requisicao dos dados
    soup = BeautifulSoup(source_code, 'html.parser')

    # Text is given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        #Transforma em string
        content = each_text.text


        #Transforma em letras minusculas e divide por linha
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        symbols = '!@#$%*()_-|\:;<>?{}[]+,'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    #Apresenta as palavras com maior ocorrencia no site
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print('% s : % s ' % (key, value))

    c = Counter(word_count)


    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')
