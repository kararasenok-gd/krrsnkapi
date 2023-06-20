import requests
import json
import random

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

		url = f'https://kararasenok.ueuo.com/api/v1/runphpscript/?apikey={self.apikey}&code={self.code}'

		self.response = requests.post(url)

		return self.response.text

class r34:
	def __init__(self, apikey):
		self.apikey = apikey

	def get_url(self, keyword, page = 0, use_r34_api = False):
		self.keyword = keyword
		self.page = page
		self.use_r34_api = use_r34_api

		if self.use_r34_api is False:
			self.response = requests.post(f"https://kararasenok.ueuo.com/api/v1/r34/?keyword={self.keyword}&apikey={self.apikey}&page={self.page}")
		else:
			self.response = requests.post(f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={self.keyword}&pid={self.page}&json=1&limit=1000")

		return self.response.text

	def get_img_link(self, json_data):
		self.json_data = json_data

		self.data = json.loads(self.json_data)

		self.random_object = random.choice(self.data)

		self.random_fileurl = self.random_object['file_url']

		return self.random_fileurl
