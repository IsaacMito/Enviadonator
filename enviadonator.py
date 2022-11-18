import urllib.parse

from bss import Bss
from chrome import Chrome
from excel import Excel

class Enviadonator:

    def __init__(self, excel: Excel, mensagem: str, cod_campanha):
        self.bss = Bss()
        self.chrome = Chrome()
        self.excel = excel
        self.mensagem: str = mensagem
        self.cod_campanha = cod_campanha


    def start(self):

        for row in range(1, self.excel.max_row + 1):

            celular = self.excel.get_celular(row)
            nome = self.excel.get_nome(row)
            status = self.excel.get_status(row)

            entity = self.bss.get_entity("619" + celular, self.cod_campanha)

            if status is None and len(entity) == 0:

                msg = self.mensagem.replace('{nome}', nome)
                msg = urllib.parse.quote(msg)

                if self.chrome.pesquisar(celular, msg):

                    self.chrome.enviar()

                    self.bss.create("619" + celular, self.cod_campanha)
                    self.excel.set_status('Enviado', row)
                else:
                    self.excel.set_status('Nao encontrado', row)

                self.excel.salvar()