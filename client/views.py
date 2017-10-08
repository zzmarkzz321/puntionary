# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from client import client
from nlp import process_text
import requests
import json

@client.route('/')
def index():
	return render_template('index.html')

@client.route('/punny', methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		datas = request.json
		print(datas)
		# Grab the keywords from the NLP framework
		try:
			response = process_text(str(datas['key']))
		except:
			response = process_text(str(datas['firstParam']))

		payload = []
		for p in response:
			payload.append(p)

		payload = jsonify(payload=payload)
		try:
			params = json.loads(payload.data)
		except:
			params = jsonify(payload='')
		# Filter and query the correct puns for the respective keyword(s)
		response = requests.get('http://localhost:5000/api/v1/puns', params=params, headers = {'Access-Control-Request-Method': 'GET', 'Access-Control-Allow-Origin': 'http://localhost:3000'})

		try:
			res = json.loads(response.text)
			# print(res)
		except:
			res = jsonify(response='')
			# print(res)
		print(res)
		# return jsonify(response=response), 200
		return jsonify(res=res), 200

	return 'it works'

# ====================
