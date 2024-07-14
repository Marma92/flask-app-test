#!/bin/python3

from flask import Flask, request, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Définir une ressource API
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

class User(Resource):
    def get(self, user_id):
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            return user
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        global users
        users = [user for user in users if user['id'] != user_id]
        return '', 204

    def put(self, user_id):
        data = request.get_json()
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            user.update(data)
            return user
        return {'message': 'User not found'}, 404

# Définir une ressource API pour la liste des utilisateurs
class UserList(Resource):
    def get(self):
        return users

    def post(self):
        data = request.get_json()
        user_id = len(users) + 1
        user = {'id': user_id, 'name': data['name']}
        users.append(user)
        return user, 201

# Ajouter les ressources API aux routes
api.add_resource(HelloWorld, '/api')
api.add_resource(User, '/api/user/<int:user_id>')
api.add_resource(UserList, '/api/users')


if __name__ == '__main__':
    app.run(debug=True)