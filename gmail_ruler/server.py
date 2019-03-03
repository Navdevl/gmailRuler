from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from core.ruler import Ruler

app = Flask(__name__)
api = Api(app)
ruler = Ruler()

class RulerServer(Resource):
  def post(self):
    json_data = request.get_json(force=True)
    count = ruler.apply(**json_data)
    return {"emails_updated": count}

api.add_resource(RulerServer, '/')
