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
    keywords = request.args

    keywords = keywords.to_dict()
    # keyword = keywords[0]
    print(keywords)
    try:
        keyword = keywords['payload']
        query = jsonify({
            "keyword": keyword
        })
        print(query.data)
        res = requests.get('https://api.mlab.com/api/1/databases/puns/collections/puns?apiKey=QMnAIvg_hFPN4adkAb5hrWn1tU1QZafQ&f={"phrase":1}&q=%s' % (query.data))
        # res = requests.get('https://api.mlab.com/api/1/databases/puns/collections/puns?q={"keyword":"' + keyword + '"}&apiKey=QMnAIvg_hFPN4adkAb5hrWn1tU1QZafQ')
        # print 'response from server:', res.text
        # serverResponce = res.json()
        print(type(res.text))

        if res.text != '[  ]':
            print('if')
            response = json.loads(res.text)
        else:
            print('else')
            response = [{
                'phrase': 'This is sodapressing. Looks like I don\'t have a pun for that! (Yet). Teach me some puns to help others!'
            }]
    except:
        # Default in case no key words are included
        print('INSIDE EXCEPT')
        response = [{
            'phrase': 'This is sodapressing. Looks like I don\'t have a pun for that! (Yet). Teach me some puns to help others!'
        }]
    # keywords = ['dairy']

    # query = {'$or': []}
    # for keyword in keywords:
    #     query['$or'].append({'keyword': keyword})

    # Replace with the response
    return jsonify(response=response), 200

# ====================
