from flask import Flask
from flask_restful import Api, Resource
import requests
import os
import math

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Lcm(Resource):
    
    def get(self, num1, num2):
        x = int(num1)
        y = int(num2)
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm



api.add_resource(Lcm, '/<int:num1>/<int:num2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=6009,
        host="0.0.0.0"
    )
