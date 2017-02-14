#! /usr/bin/env python
#! -*- coding: utf8 -*-

from flask_restful import Api, Resource, reqparse, fields, marshal
from flask import Flask, jsonify, abort, make_response

from controller.produto import ProdutoAPI, ProdutoListAPI
from controller.servico import ServicoAPI, ServicoListAPI
from controller.safra import SafraAPI, SafraListAPI

app = Flask(__name__, static_url_path="")
api = Api(app)


''' Definição de link das URLs com a API Controller... '''
api.add_resource(ProdutoListAPI, '/api/safra')
api.add_resource(ProdutoAPI, '/api/safra/<int:id>')

api.add_resource(ServicoListAPI, '/api/servico')
api.add_resource(ServicoAPI, '/api/servico/<int:id>')

api.add_resource(SafraListAPI, '/api/produto')
api.add_resource(SafraAPI, '/api/produto/<int:id>')


if __name__ == '__main__':
	app.run(port=5471, debug=True)
