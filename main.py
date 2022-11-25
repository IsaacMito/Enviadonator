from excel import Excel
from enviadonator import Enviadonator

mensagem = """⚫🟡⚫🟡⚫🟡⚫🟡
*CALCE PERFEITO*
*COMEÇOU BLACK FRIDAY*

Produtos com até 
*50% DE DESCONTO*

E isso mesmo!

*METADE DO PREÇO*

Usaflex, Skechers, 
Piccadilly, Opanankem
e muito mais
🩴🥿👠👡👢


Venha tomar um delicioso café conosco e saia daqui com seu presente prontinho.
🎁🍾🥂"""

cod_campanha:int = 1

excel:Excel = Excel(r"Y:\09 Area pessoal\9.5 Isaac\Calce Perfeito - CONTATOS\2022-11-22\AsaSul.xlsx")

Enviadonator(excel, mensagem, cod_campanha).start()












