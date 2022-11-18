import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Chrome:

    def __init__(self):

        file = open("session.txt")
        session_id = file.readline()

        if len(session_id) == 0:

            self.navegador = webdriver.Chrome(port=9515)

            file = open('session.txt', 'w')
            file.write(self.navegador.session_id)

        else:
            try:
                self.navegador = webdriver.Remote(command_executor="http://127.0.0.1:9515")
                self.navegador.close()
                self.navegador.session_id = session_id
            except:
                file = open("session.txt", 'w')
                file.write("")
                self.__init__()

        self.navegador.get(f"https://web.whatsapp.com/")

        while len(self.navegador.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)

    def pesquisar(self, numero="", mensagem=""):

        self.navegador.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")

        while len(self.navegador.find_elements(by=By.ID, value="side")) < 1:
            time.sleep(1)

        time.sleep(4)

        if len(self.navegador.find_elements(by=By.CLASS_NAME, value="_3J6wB")) == 0:
            return True

        return False

    def enviar(self):
        self.navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(Keys.ENTER)
        time.sleep(2)