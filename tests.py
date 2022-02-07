
from bs4 import BeautifulSoup
from flask import Flask
import requests
import pytest
import time
import pandas as pd



url = 'http://localhost:8000'



def soup(request):
    r=request.text
    return BeautifulSoup(r, 'html.parser')


def test_should_return_404():
	response = requests.get(url+"/test")
	assert response == 404

def test_should_status_code_ok():
	
	response = requests.get(url)
	assert response.status_code == 200



def test_should_return_data():

	file =open("immo_CSV.csv","rb")
	requests.post(url,file.read())

	data_normal=pd.read_csv('static/immo_CSV.csv',delimiter=";")
	data=pd.read_csv('immo_CSV.csv',delimiter=";")
	assert data == data_normal
	response = requests.get(url+"/data_view")
	assert response == 200
	#print(response)
	s=soup(response)
	#print(s)
	res=s.find(id="prediction")
	assert '[(1, "59_0_Lalcve_Bouygues, 3, Appartement, 178823.0, 203400.5687, 169500.47, 2849.71, 3419.65, N, False, False, False, 1, Clermont-Ferrand, 63, aout 2023, 91 RUE DE LA GANTIERE 63000 Clermont-Ferrand, datetime.date(2021, 7, 21))]' in res.replace('"','').replace("'",'')


test_should_return_data()