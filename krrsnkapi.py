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

	def get_last_message_info(self, wReturn):
		self.wReturn = wReturn

		url = f'https://kararasenok.ueuo.com/api/v1/getlastmessageinfo/?apikey={self.apikey}&return={self.wReturn}'

		self.response = requests.post(url)
	

		self.status = self.response.text

		return self.status

	def get_message_by_id(self, msgid, returnMessage = "0"):
		self.msgid = msgid
		self.returnMessage = returnMessage

		url = f'https://kararasenok.ueuo.com/api/v1/getmessagebyid/?apikey={self.apikey}&id={self.msgid}&returnMessage={self.returnMessage}'

		self.response = requests.post(url)
	

		self.status = self.response.text

		return self.status

	def get_message_info_by_id(self, msgid, wReturn):
		self.msgid = msgid
		self.wReturn = wReturn

		url = f'https://kararasenok.ueuo.com/api/v1/getmessageinfobyid/?apikey={self.apikey}&id={self.msgid}&return={self.wReturn}'

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

class PHPsandbox:
	def __init__(self, apikey):
		self.apikey = apikey

	def create_code(self, code):
		self.code = code

		self.code = self.code.replace("\n", " ")

		url = f'https://kararasenok.ueuo.com/api/v1/runphpscript/?apikey={self.apikey}$code={self.code}'

		self.response = requests.post(url)

		return self.response.text
