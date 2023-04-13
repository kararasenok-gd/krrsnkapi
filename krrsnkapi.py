import requests

class Chat:
	def __init__(self, apikey):
		self.apikey = apikey

	def send_message(self, message):
		self.message = message

		url = f'https://kararasenok.ueuo.com/api/v1/addchatmessage/?message={self.message}&apikey={self.apikey}'

		self.response = requests.post(url)
	

		self.status = self.response.text

		return self.status

class Base64:
		def __init__(self, apikey):
			self.apikey = apikey

		def decode(self, text):
			self.text = text

			url = f'https://kararasenok.ueuo.com/api/v1/base64/decode/?text={self.text}&apikey={self.apikey}'

			self.response = requests.post(url)

			return self.response.text

		def encode(self, text):
			self.text = text

			url = f'https://kararasenok.ueuo.com/api/v1/base64/encode/?text={self.text}&apikey={self.apikey}'

			self.response = requests.post(url)

			return self.response.text

