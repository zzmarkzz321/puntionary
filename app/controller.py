from flask import url_for, redirect, render_template, flash, g, session, request, jsonify
from app import app
import requests

@app.route('/testing')
def testing():
	print('get receinved!')

	return jsonify(text='goods'), 200