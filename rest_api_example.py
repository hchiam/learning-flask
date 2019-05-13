# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3?gi=29c8e338d032
# python3 -m venv venv
# . venv/bin/activate
# pip install Flask
# python rest_api_example.py # or python3 rest_api_example.py
# http://localhost:5000/user/Jane
# http://localhost:5000/user/John

from flask import Flask, render_template, redirect, url_for
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

users = [
    {
        'name':'Jane',
        'age':42,
        'job':'Engineer'
    },
    {
        'name':'John',
        'age':32,
        'job':'Doctor'
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if (name == user['name']):
                return user, 200
        return 'User not found', 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('job')
        args = parser.parse_args()
        for user in users:
            if (name == user['name']):
                return 'User with name {} already exists'.format(name), 400
        user = {
            'name':name,
            'age':args['age'],
            'job':args['job']
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('job')
        args = parser.parse_args()
        for user in users:
            if (name == user['name']):
                user['age'] = args['age']
                user['job'] = args['job']
                return user, 200
        user = {
            'name':name,
            'age':args['age'],
            'job':args['job']
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user['name'] != name]
        return '{} is deleted'.format(name), 200

api.add_resource(User, '/user/<string:name>')
app.run(debug=True)