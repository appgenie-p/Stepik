import re


stich = "Я к вам пишу - чего_же боле?"

res = re.sub(r"\-", '', stich)

print(res)