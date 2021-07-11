from wit import Wit
from colorama import Fore, Back, Style, init
import requests

class Easygit:
	def __init__(self, access_token="KLQTSWHCTIEB2H527HH4GAPXN7HXQLP6"):
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
			self.red_print("Internet Connection Required\n")

	def process(self,text):
		if text == 'dashboard_features':
			self.green_print("git clone <repo>")						

	def green_print(self,text):
		print(Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL)

	def red_print(self,text):
		print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)

	def magenta_print(self,text):
		print(Fore.MAGENTA + Style.BRIGHT + text + Style.RESET_ALL)

	def yellow_print(self,text):
		print(Fore.YELLOW + Style.BRIGHT + text + Style.RESET_ALL)	

	def cyan_print(self,text):
		print(Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL,end=" ")	

	def get_result(self,intent_name):
		URL = "https://raw.githubusercontent.com/Sharan-Babu/easygit/main/easygit/new_intents.txt"
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
		self.magenta_print("Interactive mode:")
		while True:
			self.cyan_print("\nEnter your query:")
			query = input()
			if query.lower() == 'quit':
				self.magenta_print("You exited interactive mode")
				break
			else:
				self.query(query)	
