# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from app import app
import requests

@app.route('/api/v1/puns')
def toggle_complete():
    # keywords = request.get.args['payload']['payload']
    # query = {$or: []}
    # for keyword in keywords:
    #     query['$or'].append({'keyword': keyword})
        
    res = requests.get('https://api.mlab.com/api/1/databases/puns/collections/puns?apiKey=QMnAIvg_hFPN4adkAb5hrWn1tU1QZafQ')
    # print 'response from server:', res.text
    # serverResponce = res.json()
    print(res.text)

    return jsonify({'test': 'test'}), 200

# ====================