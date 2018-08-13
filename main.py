#!flask/bin/python
# -*- coding: utf-8 -*-

import random
from functools import wraps
import json
from flask import Flask, jsonify, render_template, request, abort, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
	return render_template('index.html')

@app.route("/keyboard")
def main_key():
	target_json = {
		"type" : "buttons",
		"buttons" : ["도움말"]
	}
	return jsonify(target_json)

@app.route("/message", methods = ['POST'])
def return_func():
	target_json = {}
	msg_content = request.get_json() # user_key, type, content
	if msg_content["content"].startswith("도움말"):
		target_json["message"] = {
			"text" : "아직 도움말이 없어!"
		}
	else :
		target_json["message"] = {
			"text" : "무슨 말인지 모르겠어! 도움이 필요하면 \"도움말\"이라고 해줘!"
		}

	return jsonify(target_json)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=7700,debug=True)
