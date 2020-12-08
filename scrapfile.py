import requests
from bs4 import BeautifulSoup
import numpy as np
import re, json, csv

class Scrap:
	def __init__(self, query):
		self.query = query
		print("Searching Websites...")
	def displaylink(self): # links
		web1 = f"https://www.jadroo.com/search/products?search={self.query}"
		web2 = f"https://www.clickbd.com/search?q={self.query}"
		web3 = f"https://www.othoba.com/src?q={self.query}"
		return web1, web2, web3

	def websites(self): # function for only websites
		sit_html = []
		web = self.displaylink() # call all site
		site_list = [i for i in web] # site appending 
		for j in range(len(site_list)): 
			r = requests.get(site_list[j]).text # request to get webpage and get text
			sit_html.append(r)
		# print(sit_html)
			# print(r)
		return r, site_list, sit_html

#######################################################
# Jadroo.com
	def ScrapJadroo(self):
		myData = self.websites()[2] # 
		soup = BeautifulSoup(myData[0], "html.parser")
		image_link = []
		datas_jadroo = []
		name_of_product_jadroo = []
		price_of_product_jadroo = []
		for dc in soup.find_all('div', {'class': 'image'}):
			for cc in dc.find_all('a'):
				for gg in cc.find_all('img'):
					image_link.append(gg["src"])
		# name of product jadroo
		for name_of_prod in soup.find_all('div', {'class': 'product-info text-left'}):
			for names_item in name_of_prod.find_all('h3', {'class': 'name'}):
				for items_name in names_item.find_all('a'):
					item_jadroo = str(items_name).split(">")[1].split('</a')[0]
					name_of_product_jadroo.append(item_jadroo)
		 # price of product jadroo
		for prod_price in soup.find_all('div', {'class': 'product-price'}):
			for jadroo_price in prod_price.find_all("span", {'class': 'price'}):
				price_of_product_jadroo.append(int(str(jadroo_price).split()[4]))

		for i in range(len(image_link)):
			data = {
				"id": int(i),
				"links": image_link[i],
				"name_of_product": name_of_product_jadroo[i],
				"price_of_product": price_of_product_jadroo[i]
			}
			datas_jadroo.append(data)
		# print(datas_jadroo)
		with open("data_jadroo.json", "w") as jadroo_file:
			json.dump(datas_jadroo, jadroo_file)
		# print(datas_jadroo)
		# print("\n\n")

##################################################################
# Clickbd.com
	def Clickbd(self):
		clickbd = self.websites()[2]
		soup_click = BeautifulSoup(clickbd[1], "html.parser")
		image_link_clickbd = []
		datas_clickbd = []
		name_of_product_clickbd = []
		price_of_product_clickbd = []
		for cbd in soup_click.find_all('div', {'class': 'img'}):
			for img_bd in cbd.find_all('img'):
				image_link_clickbd.append(img_bd["src"])
		# name of product for clickbd
		for price_bd in soup_click.find_all('div', {'class': 'lt'}):
			for price in price_bd.find_all("h3"):
				for tit in price.find_all("a"):
					name_of_product_clickbd.append(tit["title"])

		# price of product for clickbd
		for price_clickbd in soup_click.find_all('div', {'class': 'rt'}):
			for real_price_clickbd in price_clickbd.find_all("b"):
				for p in real_price_clickbd.find_all("b"):
					processed = str(p).split("<b>")[1].split("</b>")[0].replace(',', '')
					price_of_product_clickbd.append(processed)


		for j in range(len(image_link_clickbd)):
			data_click = {
				"id": int(j),
				"links": image_link_clickbd[j],
				"name_of_product": name_of_product_clickbd[j],
				"price_of_product": price_of_product_clickbd[j]
			}
			datas_clickbd.append(data_click)
		# print(datas_clickbd)
		with open("data_click.json", "w") as click_file:
			json.dump(datas_clickbd, click_file)
		# print(datas_clickbd)
		# print('\n\n')

################################################################
# Othoba.com
	def Othoba(self):
		othoba = self.websites()[2]
		othoba_data = BeautifulSoup(othoba[2], "html.parser")
		image_link_othoba = []
		datas_othoba = []
		name_of_product_othoba = []
		price_of_product_othoba = []
		for m in othoba_data.find_all('div', {'class': 'picture bs-quick-view'}):
			for bn in m.find_all('a'):
				for po in bn.find_all('img'):
					image_link_othoba.append(po["data-src"])
		#name of product
		for othoba_det in othoba_data.find_all('div', {'class': 'details'}):
			for othoba_name in othoba_det.find_all('h2', {'class': 'product-title'}):
				for link_name in othoba_name.find_all('a'):
					name_list = (str(link_name).split('<a')[1].split('>')[1].split('</a')[0])
					name_of_product_othoba.append(name_list)
		#price othoba
		for othoba_price in othoba_data.find_all('div', {'class': 'add-info'}):
			for price_othoba in othoba_price.find_all('div', {'class': 'prices'}):
				for actual_price in price_othoba.find_all('span', {'class': 'price actual-price'}):
					price_othoba = (str(actual_price).split('<span class="price actual-price">')[1].split('</span>')[0]).replace("Tk ", "")
					price_of_product_othoba.append(price_othoba)

		price_of_product_othoba_clear = []
		for cleaning in range(len(price_of_product_othoba)):
			if price_of_product_othoba[cleaning].isnumeric() == False:
				price_of_product_othoba_clear.append(price_of_product_othoba[cleaning])
				name_of_product_othoba.remove(name_of_product_othoba[cleaning])
				image_link_othoba.remove(image_link_othoba[cleaning])

		for clear_value in price_of_product_othoba_clear:
			price_of_product_othoba.remove(clear_value)
		print(price_of_product_othoba)

		for a in range(len(image_link_othoba)):
			data_othoba = {
			"id": int(a),
			"links": image_link_othoba[a],
			"name_of_product": name_of_product_othoba[a],
			"price_of_product": price_of_product_othoba[a]
			}
			datas_othoba.append(data_othoba)
		print(datas_othoba)
		with open("data_othoba.json", "w") as othoba_file:
			json.dump(datas_othoba, othoba_file)
			
		# print(datas_othoba)