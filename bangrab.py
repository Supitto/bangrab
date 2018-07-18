#!/usr/bin/python3

"""mini programa de banner grabbing"""

from sys import argv

import shodan
import json
import hashlib
import os

hasher = hashlib.md5()

def md5(raw):
	hasher.update(raw)
	return hasher.hexdigest()

def find_dup(arr):
	hashes = []
	dup = []
	for i in range(len(arr)):
		hash = md5(arr[i])
		if hash in hashes:
			dup.append(i)
		else:
			hashes.append(hash)
	return dup

if __name__ == "__main__":

	if len(argv) < 3 or argv[1] == '-h':
		print("Uso: bangrap.py [SHODAN_KEY] [QUERY PARAMETERS]")

	#Obtem a informação basica
	key = argv[1] #input("Por favor insira sua chave do shodan : ")
	query = argv[2] #input("Insert the search query : ")
	
	#Realiza a busca
	api = shodan.Shodan(key)
	results = api.search(query)

	#Extrai os resultados
	print("Foram recuperados "+str(results['total'])+" banners")
	arr = [results['matches'][i]['data'] for i in range(len(results['matches']))]
	
	print("Realizando eliminação de duplicatas")
	duplicatas = find_dup(arr)
	#O proximo for funciona porque estou iterando um slice, e não a lista original
	#[::-1] retorna a lista invertida
	#Ao inverter a lista de duplicatas os indices maiores aparecem primeiro
	#Desta forma podemos brincar livremente com os indices
	for i in duplicatas[::-1]:
		del arr[i]
	print("Foram eliminados "+str(len(dup))+" banners duplicados")

	print("Gravando os banners restantes")
	for i in range(len(arr)):
		with open('banners/banner_'+str(i)+'.txt','w') as f:
			f.write(arr[i])
