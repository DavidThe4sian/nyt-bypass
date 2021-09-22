from flask import(
	Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
import requests
from bs4 import BeautifulSoup
import json

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
	return render_template('main/index.html')

@bp.route('/', methods=['POST'])
def get_recipe():
	if request.method == 'POST':
		print('we here')
		data = request.data.decode('ascii')
		print(data)
		dataJson = json.loads(data)
		print(dataJson['url'])
		return getData(dataJson['url'])

@bp.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})

def getData(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	resultJson = soup.find('script', type='application/ld+json').get_text()
	test = json.loads(resultJson)
	json_formatted_str = json.dumps(test, indent=2)

	# print(json_formatted_str)
	return json_formatted_str
