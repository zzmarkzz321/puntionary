# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from client import client

@client.route('/hello')
def index():
	return 'hello!'

# ====================
