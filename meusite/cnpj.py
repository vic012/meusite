import requests as http

class CNPJ:

	def __init__(self, cnpj):
		self.__cnpj = cnpj
		self.__resultado = []

	def valida(self):
		if (not len(self.__cnpj) == 14):
			pyg.alert('Por favor, digite um número de CNPJ válido!')
			self.__cnpj = None
			exit()
		else:
			return self.__cnpj


	def consulta(self):
		cabecalho_api = {'Content-Type': 'application/json'}
		api = http.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(self.valida()), cabecalho_api)
		status = api.json()['status']
		if (status == 'ERROR'):
			pyg.alert('O CNPJ informado é invalido!')
		else:
			self.__resultado.append(api.json())
	@property	
	def demonstra(self):
		return self.__resultado

'''teste = CNPJ('34983867000126')
teste.consulta()

print(teste.demonstra)'''