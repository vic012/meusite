import requests as http

class CNPJ:

	def __init__(self, cnpj):
		self.__cnpj = cnpj
		self.__resultado = None

	def consulta(self):
		if (type(self.__cnpj) == 'int') or (len(self.__cnpj) == 14):
			cabecalho_api = {'Content-Type': 'application/json'}
			api = http.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(self.__cnpj, cabecalho_api))
			status = api.json()['status']
			if (status == 'ERROR'):
				self.__resultado = 'Por favor, verifique se o número digitado está correto'
			else:
				self.__resultado = api.json()
		else:
			self.__resultado = 'Por favor, Insira um cnpj com 14 dígitos e sem . / ou -'
		
	@property	
	def demonstra(self):
		return self.__resultado

'''teste = CNPJ('00776574000660')
teste.consulta()

print(teste.demonstra)'''