#! /usr/bin/env python
#! -*- coding: utf8 -*-

from flask_restful import Api, Resource, reqparse, fields, marshal

class ServicoAPI(Resource):

	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('title', type=str, location='json')
		self.reqparse.add_argument('done', type=bool, location='json')
		self.reqparse.add_argument('description', type=str, location='json')

		super(ServicoAPI, self).__init__()

	def get(self, id):
		return {'result': True}

	def put(self, id):
		return {'result': True}

	def delete(self, id):
		return {'result': True}

class ServicoListAPI(Resource):
    def get(self):
        return {'result': True}

    def post(self):
        return {'result': True}
