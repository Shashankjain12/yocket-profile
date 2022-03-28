import logging

import werkzeug
from flask import request
from flask_restx import Resource, reqparse

from api.caas.functions import get_posts, create_user, get_users, create_post, get_comments, create_comment
from api.caas.serializers import users_input, users_output, posts_input, posts_output, commented_fields_output, commented_fields_input, posts_created, comments_created
from api.restplus import api

logger = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to users management')

@ns.route('/')
class UsersCollection(Resource):
    @api.expect(users_input)
    @api.response(201, 'User creation initiated', users_output)
    def post(self):
        """
        Create a user
        """
        data = request.json
        result, code = create_user(data)
        return result, code
    
    @api.marshal_with(users_output, as_list=True)
    def get(self):
        """
        Get a list of all users.
        """
        users = get_users()
        return users
    