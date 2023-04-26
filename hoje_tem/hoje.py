"""
Este programa tem como finalidade buscar na Wikipedia em português os eventos, 
datas comemorativas, aniversários e obtuários da data atual.
"""

import requests

from datetime import date as dt

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from hoje_tem.transforma_data import TransformaData


def data_atual():
    """
    Pega a data atual e a transforma em uma data por extenso.
    """
    data = dt.today().strftime('%d-%m-%Y')
    return TransformaData().dataExtensoBr(data)
    

def monta_url():
    """
    Gera uma URL para a Wikipedia com base na data atual.
    """
    dia = data_atual()
    return f"https://pt.wikipedia.org/wiki/{dia}"

def motorista():
    """
    Instancia o driver do navegador, busca o DOM da URL passada e 
    retorna o objeto referente à página.
    """
    url = monta_url()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    return driver

def nascidos():
    """
    Busca dentro do DOM os dados referentes aos nascimentos dentro da página
    e retorna os nomes e os anos de nascimento das pessoas.
    """
    datas = ""
    elementos = motorista().find_elements(
                                        By.XPATH, 
                                        '//ul[preceding-sibling::h2/span[contains(text()'\
                                        ', "Nascimentos")] and following-sibling::h2/span'\
                                        '[contains(text(), "Mortes")]]'
                                        )
    for elemento in elementos:
        datas += elemento.text
    return datas

def verifica_status():
    """ Verifica se o HTTP status é 200 - OK. """
    return requests.get(monta_url())


if __name__ == "__main__":
    assert verifica_status().status_code == 200
    print(nascidos())