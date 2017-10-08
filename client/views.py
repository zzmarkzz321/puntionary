# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from client import client
from nlp import process_text
import requests

@client.route('/')
def index():
	return render_template('index.html')

@client.route('/test', methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		datas = request.json
		# Grab the keywords from the NLP framework
		response = process_text(str(datas['key']))

		payload = []
		for p in response:
			payload.append(p)
		
		payload = jsonify(payload=payload)
		print(payload.data)
		# Filter and query the correct puns for the respective keyword(s)
		response = requests.get('http://localhost:5000/api/v1/puns', params=payload.data, headers = {'Access-Control-Request-Method': 'GET', 'Access-Control-Allow-Origin': 'http://localhost:3000'})

		print(response.text)
		# return jsonify(response=response), 200
		return jsonify({'test': 'cool!'}), 200

	return 'it works'

# ====================
