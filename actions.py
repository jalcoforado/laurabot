# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# importe a biblioteca usada para consultar uma URL
import urllib.request

# importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup
import pandas as pd
import sys

# especifique o URL
class action_get_prefeito(Action):
    def name(self):
        return "action_get_prefeito"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        Cidade = tracker.get_slot("cidade")
        print(Cidade)
        Cidade = str(Cidade).upper()
        # especifique o URL
        wiki = "https://pt.wikipedia.org/wiki/Lista_de_prefeitos_dos_munic%C3%ADpios_mais_populosos_do_Brasil"
        # Consulte o site e retorne o html para a variável 'page'
        page = urllib.request.urlopen(wiki)
        # Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
        soup = BeautifulSoup(page, "html.parser")
        # Localiza a table dos nomes do prefeito
        table = soup.find("table", class_="wikitable sortable")
        A = []
        B = []
        C = []
        D = []
        E = []

        for row in table.findAll("tr"):  # para tudo que estiver em <tr>
            cells = row.findAll("td")  # variável para encontrar <td>
            if len(cells) == 5:  # número de colunas
                A.append(cells[0].find(text=True))  # iterando sobre cada linha
                B.append(str(cells[1].find("a").text).upper())
                C.append(cells[2].find("a").text)
                D.append(cells[3].find(text=True))
                E.append(cells[4].find(text=True))

        df = pd.DataFrame(index=A, columns=["Posição"])

        df["Posição"] = A
        df["Cidade"] = B
        df["Estado"] = C
        df["Prefeito"] = D
        df["Partido"] = E
        if Cidade == "none":
            dispatcher.utter_message(text="Cidade invalida!")

        else:
            resposta = df[df["Cidade"] == Cidade]

            # resposta = str(resposta)
            print(resposta)
            resposta_final = resposta["Prefeito"].values[0] + " do partido " + resposta["Partido"].values[0]
            print(str(resposta_final))
            dispatcher.utter_message(str(resposta_final))
