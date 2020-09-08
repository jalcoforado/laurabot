from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
#importe a biblioteca usada para consultar uma URL
import urllib.request
#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup
import pandas as pd
import sys
#especifique o URL
class ActionGetPrefeito(Action):
    def name(self):
        return "get_prefeito"
    def run(self, dispatcher, tracker, domain):

        Cidade = tracker.get_slot('Cidade')
        #especifique o URL
        wiki = "https://pt.wikipedia.org/wiki/Lista_de_prefeitos_dos_munic%C3%ADpios_mais_populosos_do_Brasil"
        #Consulte o site e retorne o html para a variável 'page'
        page = urllib.request.urlopen(wiki)
        #Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
        soup = BeautifulSoup(page, 'html.parser')
        #Localiza a table dos nomes do prefeito
        table = soup.find('table', class_='wikitable sortable')
        A=[]
        B=[]
        C=[]
        D=[]
        E=[]

        for row in table.findAll("tr"): #para tudo que estiver em <tr>
            cells = row.findAll('td') #variável para encontrar <td>
            if len(cells)==5: #número de colunas
                A.append(cells[0].find(text=True)) #iterando sobre cada linha
                B.append(cells[1].find('a').text)
                C.append(cells[2].find('a').text)        
                D.append(cells[3].find(text=True))
                E.append(cells[4].find(text=True))

        df = pd.DataFrame(index=A, columns=['Posição'])

        df['Posição']=A
        df['Cidade']=B
        df['Estado']=C
        df['Prefeito']=D
        df['Partido']=E
        if Cidade == '':
            print(df)
        else:
            resposta = df[df['Cidade']==Cidade]
            print(str(resposta['Prefeito'].values), " Do partido ", str(resposta['Partido'].values))