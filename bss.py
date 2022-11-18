import cx_Oracle
from cx_Oracle import Cursor


class Bss:

    def __init__(self):

        cx_Oracle.init_oracle_client(lib_dir=r'./client/instantclient_21_3')

        self.connection = cx_Oracle.connect(

            user='click', password='falaae',
            dsn='mocassim.calceperfeito.com.br/orcl',
            encoding='UTF-8'
        )

    def get_entity(self, celular, cod_campanha):

        cursor: Cursor = self.connection.cursor()

        sql = f"SELECT * FROM ENVIO_WHATSAPP WHERE NUMERO = {celular} AND COD_CAMPANHA = {cod_campanha} AND ROWNUM = 1"

        result = tuple(cursor.execute(sql))

        cursor.close()

        return result

    def create(self, celular, cod_campanha):

        cursor: Cursor = self.connection.cursor()

        sql = f"INSERT INTO CLICK.ENVIO_WHATSAPP (COD_CAMPANHA, NUMERO) VALUES({cod_campanha},{celular})"

        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
