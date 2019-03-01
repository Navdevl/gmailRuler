from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
  def post(self):
    json_data = request.get_json(force=True)
    return json_data

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
  app.run(debug=True)
