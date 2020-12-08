import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
from selenium import webdriver


driver = webdriver.Firefox()

url = "https://www.amazon.com"
driver.get(url)