import json

file_name = "data.json"
directory_data = "../media/files/"

class Data_Base:
	def __init__(self):
		with open(directory_data + file_name) as json_file:
			donnees = json.load(json_file)
		self.donnees = donnees
