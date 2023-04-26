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

    data = dt.today().strftime('%d-%m-%Y')
    hoje = TransformaData().dataExtensoBr(data)
    return hoje

def monta_url():
    return f"https://pt.wikipedia.org/wiki/{data_atual()}"

def motorista():
    url = monta_url()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    return driver

def nascidos():
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

def check_status():
    status = requests.get(monta_url())
    return status

if __name__ == "__main__":
    assert check_status().status_code == 200
    print(nascidos())