# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from forms import ExampleForm, LoginForm
from models import User

@app.route('/api/v1/puns')
def toggle_complete():
    keywords = request.get.args['payload']['payload']
    query = {$or: []}
    for keyword in keywords:
        query['$or'].append({'keyword': keyword})
        
    res = requests.post('https://api.mlab.com/api/1/databases/puns/collections/puns?apiKey=QMnAIvg_hFPN4adkAb5hrWn1tU1QZafQ&f={"phrase": 1}&q=%s' % (query))
    print 'response from server:', res.text
    serverResponce = res.json()

    return jsonify({'test': 'test'}), 200

# ====================