# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from app import app
import requests
import json

@app.route('/api/v1/puns')
def toggle_complete():
    # keywords = request.args
    # keywords = ['dairy']
    # query = {'$or': []}
    # for keyword in keywords:
    #     query['$or'].append({'keyword': keyword})

    query = jsonify({
        "$or": [
            {"keyword":"taco"},
            {"keyword":"soda"}
        ]
    })

    res = requests.get('https://api.mlab.com/api/1/databases/puns/collections/puns?apiKey=QMnAIvg_hFPN4adkAb5hrWn1tU1QZafQ&f={"phrase":1}&q=%s' % (query.data))
    # res = requests.get('https://api.mlab.com/api/1/databases/puns/collections/puns?q={"keyword":"' + keyword + '"}&apiKey=QMnAIvg_hFPN4adkAb5hrWn1tU1QZafQ')
    # print 'response from server:', res.text
    # serverResponce = res.json()
    print(res.text)

    response = json.loads(res.text)

    # Replace with the response
    return jsonify(response=response), 200

# ====================