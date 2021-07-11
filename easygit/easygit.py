from wit import Wit
from colorama import Fore, Back, Style, init
import requests


class Easygit:
	def __init__(self, access_token="TG2TPBING3AATILZB5KZN4DKRPRTEARE"):
		self.access_token = access_token
		self.client = Wit(access_token)
		self.intent_list = {"name1","name2","dashboard_features"}
		init()

	def query(self,text):
		try:
			response = self.client.message(text)
			intent_length = len(response['intents'])
			if intent_length == 0:
				intent = "Try another query"
				self.red_print(intent)
			else:	
				intent = response['intents'][0]['name']
				if intent in self.intent_list:
					self.process(intent)
				else:
					self.get_result(intent)
		except:
			self.cyan_print("Internet Connection Required")

	def process(self,text):
		if text == 'dashboard_features':
			self.green_print("git clone <repo>")						

	def green_print(self,text):
		print(Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL)

	def red_print(self,text):
		print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)

	def yellow_print(self,text):
		print(Fore.YELLOW + Style.BRIGHT + text + Style.RESET_ALL,end=" ")

	def cyan_print(self,text):
		print(Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL)	

	def get_result(self,intent_name):
		URL = "https://raw.githubusercontent.com/Sharan-Babu/Paper-Search-ElasticSearch/main/test.txt"
		req = requests.get(URL)
		req = req.text

		pos = req.find(intent_name)
		length = len(intent_name)

		start_position = pos + length + 1
		
		output = []
		while req[start_position] != ".":
			output.append(req[start_position])
			start_position += 1
		
		output = "".join(output)	
		self.green_print(output)

	def interactive(self):
		self.cyan_print("Interactive mode:")
		while True:
			self.yellow_print("\nEnter your query:")
			query = input()
			if query.lower() == 'quit':
				self.cyan_print("You exited interactive mode")
				break
			else:
				self.query(query)	
