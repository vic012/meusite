import requests as http

class Cep:

	def __init__(self, cep):
		self._cep = cep
		self._resultadoCep = None

	def validaCep(self):
		cabecalho_api = {'Content-Type': 'application/json'}
		api = http.get('https://viacep.com.br/ws/{}/json/'.format(self._cep, cabecalho_api))
		#Se o CEP não existir
		if ('erro' in api.json()):
			self._resultadoCep = 'CEP inválido'
		else:
			self._resultadoCep = api.json()
		
	@property
	def resultado(self):
		return self._resultadoCep

	
'''#para testes use:
teste = Cep('58801680')
teste.validaCep()
if (teste.resultado):
	print(teste.resultado)'''