from flask import Flask, render_template
from flask_restful import Api
import requests

from dotenv import load_dotenv

from backend import Main_Api, Files_Api

from models.database import create_db

UPLOAD_FOLDER = '/uploads'

load_dotenv()

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'fdgjj54569*FJ$84jgf@#_fdsgf8958ea52588d4b518^%jh546c20f38c5e50cbd3ca067fe9d08dc259167c63a33bb267435hj89wq8*SRF89dsgkjs8g7*(&*(&%giodsg5ten0&r(9Br37h8'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


api = Api()
api.add_resource(Main_Api, '/api/main/')
api.add_resource(Files_Api, '/api/files/')
api.init_app(app)


@app.route('/')
def Main():
    response = requests.get('http://127.0.0.1:8000/api/main/').json()
    return render_template('main.html', response=list(response['link']))


@app.route('/<code>')
def Files(code):
    json = {'code': code}
    response = requests.get('http://127.0.0.1:8000/api/main/', json=json).json()
    return render_template('files.html')


if __name__ == '__main__':
    create_db()
    app.run(host="127.0.0.1", port='8000', debug=True)