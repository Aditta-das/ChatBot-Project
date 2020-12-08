from flask import Flask
from flask import render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, redirect, url_for
from PIL import Image


import cv2, os, json, webbrowser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scrapfile import Scrap


from models import Signin
app = Flask(__name__)
app.secret_key = "super-secret-key"


@app.route("/", methods=["GET", "POST"])
def index():
	best_results = []
	if request.method == "POST":
		search = request.form.get("query")
		scrap_web = Scrap(f"{search}")
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
		# print(new_dataset)
		min_data = new_dataset[:12]
		# products = min_data["name_of_product"]
		# image = min_data["links"]
		# price = min_data["price_of_product"]
		image = [i for i in min_data["links"]]
		price = [j for j in min_data["price_of_product"]]
		title = [k for k in min_data["name_of_product"]]
		
		for j in range(len(image)):
			best = {
				"params1":
				{
				"images": image[j],
				"titles": title[j],
				"prices": price[j],
				},
			}
			# print(best)
			necessary_data = {
				"img": best["params1"]["images"],
				"tit" : best["params1"]["titles"],
				"prices_of_prod" : best["params1"]["prices"],
			}
			best_results.append(necessary_data)
			# print(necessary_data)
	return render_template('main.html', best_results=best_results)


@app.route("/licence", methods=["GET", "POST"])
def licence_plate():
	return render_template("character.html")


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
	return render_template("chatbot.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
	
	if 'user' in session and session["user"] == "Aditta":
		return render_template("character.html")

	if request.method == "POST":
		username = request.form.get("uname")
		userpass = request.form.get("pass")
		if username == "Aditta" and userpass == "1234":
			# set this session variable
			session["user"] = username
			session["pass"] = userpass
			return render_template("character.html")		
		return render_template("signin.html")

if __name__ == "__main__":
	webbrowser.open_new('http://127.0.0.1:5000/')
	app.run(debug=True)