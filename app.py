from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import model


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('phone')


@app.route('/')
def index():
    return render_template('index.html', name='Bill')


class Phone(Resource):
    def delete(self, name):
        model.delete(name)
        return '', 204

    def get(self, name):
        phone = model.read(name)
        if phone is None:
            return '', 404
        return phone[0]

    def put(self, name):
        args = parser.parse_args()
        model.update(name, args['phone'])
        return args['phone'], 201

class PhoneList(Resource):
    def post(self):
        args = parser.parse_args()
        model.create(args['name'], args['phone'])
        return args['phone'], 201

    def get(self):
        phones = model.list_()
        phones = [{'name': name, 'phone': phone} for name, phone in phones]
        return phones


api.add_resource(PhoneList, '/phones')
api.add_resource(Phone, '/phones/<name>')

if __name__ == '__main__':
    app.run(debug=True)