from flask import Blueprint
from flask_restx import Api, Resource
from models.models import User
from models.user.user_repository import UserRepository
from services.auth import UserAuth

user_controller = Blueprint('user', __name__)
api = Api(user_controller)

@api.route('/users')
class UserController(Resource):
    def post(self):
        user = api.payload
        new_user = UserRepository(User(**user)).create()
        return new_user

@api.route('/users/<int:id>')
class UserControllerWithId(Resource):
    def get(self, id):
        user = UserRepository.get_user_by_id(id)
        return user
    
    def delete(self, id):
        UserRepository.delete_user_by_id(id)
        return 'User deleted', 200


@api.route('/users/auth')
@api.route('/users/auth')
class UserAuthController(Resource):
    def post(self):
        userData = api.payload
        user_auth = UserAuth(email=userData['email'], senha=userData['senha'])
        token = user_auth.authenticate()
        return token
