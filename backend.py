from flask import jsonify, redirect, session, request
from flask_restful import Resource
from create_link import create_link
from models.files_data import Files_Data


class Main_Api(Resource):
    def get(self):
        link = create_link()
        return {'status': 'ok', 'link': link}

    def post(self):
        pass


class Files_Api(Resource):
    def get(self):
        pass