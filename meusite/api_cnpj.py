import requests
import re

class CNPJ:

	def __init__(self, cnpj=None):
		self.__cnpj = cnpj

	def _get_headers(self):
		headers = {'Content-Type': 'application/json'}
		return headers

	def _get_url(self):
		url = 'https://www.receitaws.com.br/v1/cnpj/'
		return url

	def _get_response(self, cnpj):
		headers = self._get_headers()
		url_prefix = self._get_url()
		url = f"{url_prefix}{cnpj}"
		response = requests.get(url, headers=headers)
		print(response.json())
		return response

	def consultar_cnpj(self):
		data = {}
		cnpj = self.__cnpj
		if cnpj is None:
			data["status"] = "error"
			data["message"] = 'Por favor, Insira um cnpj Válido'
			return data

		cnpj = str(cnpj)
		clean_cnpj = re.sub(r"\D", "", cnpj)

		if len(clean_cnpj) != 14:
			data["status"] = "error"
			data["message"] = f'O CNPJ: {clean_cnpj} precisa contér 14 caracteres'
			return data

		response = self._get_response(clean_cnpj)

		if response.status_code != 200:
			data["status"] = "error"
			data["message"] = f'Não foi possível consultar o {cnpj} informado'
			return data

		try:
			data_response = response.json()
		except Exception:
			data["status"] = "error"
			data["message"] = f'Não foi possível consultar o {cnpj} informado'
			return data

		status = data_response.get("status")

		if status == 'ERROR':
			data["status"] = "error"
			data["message"] = 'Por favor, verifique se o número digitado está correto'
			return data

		data["status"] = "success"
		data["content"] = data_response
		return data