import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pickle

class Chrome:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument(r"--user-data-dir=C:\Users\DEV\AppData\Local\Google\Chrome\User Data")

        self.navegador = webdriver.Chrome(options=options)
        self.navegador.get(f"https://web.whatsapp.com/")

        while len(self.navegador.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)


    def pesquisar(self, numero="", mensagem=""):

        self.navegador.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")

        while len(self.navegador.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)

        time.sleep(5)

        if len(self.navegador.find_elements(by=By.CLASS_NAME, value="_3J6wB")) == 0:
            return True

        return False

    def enviar(self):
        try:
            ref = self.navegador.find_element(By.XPATH,
                                              '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

            if ref is not None:
                ref.send_keys(Keys.ENTER)
                time.sleep(2)
        except:
            pass
