from scrapfile import Scrap
import json
import pandas as pd

def main():
	scrap_web = Scrap()
	scrap_jadroo = scrap_web.ScrapJadroo()
	scrap_clickbd = scrap_web.Clickbd()
	scrap_othoba = scrap_web.Othoba()

	json_file = ["data_jadroo.json", "data_click.json", "data_othoba.json"]
	dataset = []
	for i in range(len(json_file)):
		df = pd.read_json(f"{json_file[i]}")
		dataset.append(df)
	new_dataset = pd.concat(dataset, ignore_index=True)
	new_dataset = new_dataset.sort_values("price_of_product", axis=0, ascending=True)
	print(new_dataset)
		# with open(f"{json_file[i]}", "r") as f1:
		# 	data = f1.read()
		# obj1 = json.loads(data)

		# print(obj1)
		# price_jadroo = [jadroo["price_of_product"] for jadroo in obj1]
		# result = []
		# for jadroo in obj1:
		# 	prod = jadroo["name_of_product"]
		# 	print(prod)
		# print(json_data["price"])
		# print(f"{prod} ---> {price}")


	with open("data_click.json", "r") as f2:
		data2 = f2.read()
	obj2 = json.loads(data2)
	price_click = [click["price_of_product"] for click in obj2]

	with open("data_othoba.json", "r") as f3:
		data3 = f3.read()
	obj3 = json.loads(data3)
	price_othoba = [othoba["price_of_product"] for othoba in obj3]



if __name__ == "__main__":
	main()