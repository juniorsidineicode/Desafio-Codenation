#!/usr/bin/env python
# coding: UTF-8

import json, os, sys
import datetime, time, requests
import hashlib

my_token = 'd01b4841973fa7e9be4d157f844b054b8eee6983'
directory_OUT = os.path.realpath(os.path.dirname(__file__))+'/'
url_0 = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='+my_token
url_1 = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+my_token

response_url0 = requests.get(url_0)
dados = response_url0.content
dataout = open(directory_OUT+"answer.json", "w")
dataout.write(dados)
dataout.close()

temp = json.loads(dados)

delta_casa = temp['numero_casas'] 
cifrado = str(temp['cifrado'])
arq = open(directory_OUT+"testing.txt", "a")
arq.write(cifrado)
arq.write('\n')
arq.close

alfabeto = 'abcdefghijklmnopqrstuvwxyzab'
alfabeto2 = 'yzab'

escrever = []

novo_cifrado = []
for i in range(0, len(cifrado)):
	temp_var = cifrado[i]
	if temp_var in alfabeto:
		if (temp_var == 'a' or temp_var == 'b'):
			k = alfabeto2.index(temp_var)
			escrever = alfabeto2[k - delta_casa]
		else:		
			k = alfabeto.index(temp_var)
			escrever = alfabeto[k - delta_casa]
	if temp_var == ' ':
		escrever = ' '
	if temp_var == '.':
		escrever = '.'
	if temp_var == "'":
		escrever = "'"

	novo_cifrado.append(str(escrever))		
	arq = open(directory_OUT+"Decifrando.txt", "a")
	arq.write(escrever)
	arq.close

with open(directory_OUT + "Decifrando.txt", "r") as f:
	resposta = f.readlines()

arq = open(directory_OUT+"Decifrando.txt", "a")
arq.write('\n')
arq.close

resposta[0].replace('\n', '')

temp['decifrado'] = resposta[0]
res = hashlib.sha1(resposta[0].encode())
temp['resumo_criptografico'] = res.hexdigest()

with open(directory_OUT + "answer.json", "w") as file:
	json.dump(temp, file)
