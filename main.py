
# A very simple Flask Hello World app for you to get started with...


from flask import Flask, render_template, request, make_response, redirect, send_file, Response
from flask_cors import CORS, cross_origin
from flask import jsonify

import MySQLdb as mdb
import os
from werkzeug.utils import secure_filename
import json
import numpy as np

# import matplotlib.pyplot as plt
import datetime
import hashlib
# from cryptography.fernet import Fernet





	




### web ###########

app = Flask(__name__)
CORS(app)
# CORS(app, support_credentials=True)







@app.route("/test", methods=["get", "post"])
def NNHandler():
	return render_template('main.html', error="success", tar_c=0, tar_y='--', res_y='--', res_x=['--']*36, sum=['--']*6)
	




###### main #####

if __name__=="__main__":

	# app.run(debug=True, host="0.0.0.0", port=80)
	app.run(debug=True, host="0.0.0.0", ssl_context='adhoc')






