# -*- coding: utf-8 -*-

"""
This module the Flask REST Server and an endpoint that has the 
implementation to apply the rule. You can find the ways to communicate
with the server in the example folder provided.

"""

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from core.ruler import Ruler

app = Flask(__name__)
api = Api(app)

# Creating an instance of Ruler Class to use apply method.
ruler = Ruler()

class RulerServer(Resource):
  def post(self):
    json_data = request.get_json(force=True)
    count = ruler.apply(**json_data)
    return {"emails_updated": count}

# Adding the RulerServer as the API resource through add_resource method.
api.add_resource(RulerServer, '/')
