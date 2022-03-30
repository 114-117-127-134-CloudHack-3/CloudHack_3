from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Sub(Resource):
    def get(self, num1, num2):
        return int(num1) - int(num2)


api.add_resource(Sub, '/<int:num1>/<int:num2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5052,
        host="0.0.0.0"
    )
