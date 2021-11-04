from flask import Flask

from flask_restful import Resource, Api, reqparse
import werkzeug
from taker import taker
import datetime

app = Flask(__name__, static_folder="images")
api = Api(app)


class UploadImage(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        print(args)
        image_file = args['file']
        print('image_file')
        print(image_file)

        response = taker("images/inputs/nova.jpg", True)
        print(response)
        image_file.save(f"images/inputs/nova.jpg")
        return response
