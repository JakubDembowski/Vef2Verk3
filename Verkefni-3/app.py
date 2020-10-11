from flask import Flask, render_template, json
import urllib.request
import os 
from jinja2 import ext

app = Flask(__name__)

app.jinja_env.add_extension(ext.do)



with urllib.request.urlopen("https://apis.is/petrol/") as url:
    gogn = json.load(url.read().decode())

def format_time(gogn):
    return datetime.strptime(gogn, '%y-%m-%dT%H:%M:%S.%f').strftime('%d/%m, %Y. %H:%M')

app.jinja_env.filter['format_time'] = format_time

def minPetrol():
    minPetrolPrice = 1000
    company = None
    address = None
    lst = gogn['results']
    for i in lst:
        if i['bensin95'] is not None:
            minPetrolPrice = i['bensin95']
            company = i['company']
            address = i['name']
    return [minPetrolPrice, company, address]

@app.route('/')
def index():
    return render_template('index.html', gogn=gogn)

@app.route('/company/<company>')
def comp(company):
    return render_template('company.html', gogn=gogn, com=company)

@app.route('/moreinfo/<key>')
def info(key)
    return render_template('moreinfo.html', gogn=gogn, k=key)