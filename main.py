from excel import Excel
from enviadonator import Enviadonator

mensagem = """🔴🎄🎅🏻🔴🎄🎅🏻🔴🎄🎅🏻
*CHEEGGGOOUU O NATAL!*
*CALCE PERFEITO*

*Presentes a partir* 
*de R$ 69,99*

Conheça a nova coleção:
Sandálias da Usaflex, 
Chinelos da Piccadilly e 
Tênis da Skechers.

*Peça o nosso catálogo!*
Você vai amar!

Aguardamos você com 
café bem quentinho🥰"""

cod_campanha:int = 2

excel:Excel = Excel(r"Y:\09 Area pessoal\9.5 Isaac\Calce Perfeito - CONTATOS\2022-12-12\Guara.xlsx")

Enviadonator(excel, mensagem, cod_campanha).start()












