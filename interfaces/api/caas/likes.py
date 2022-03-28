import logging

import werkzeug
from flask import request
from flask_restx import Resource, reqparse

from api.caas.functions import get_posts, create_user, get_users, create_post, get_comments, create_comment, create_like
from api.caas.serializers import likes_input, likes_output
from api.restplus import api

logger = logging.getLogger(__name__)

ns = api.namespace('like', description='Operations related to likes management')


@ns.route('/')
class UsersCollection(Resource):
    @api.expect(likes_input)
    @api.response(201, 'Likes creation initiated', likes_output)
    def post(self):
        """
        Like a comment or Post
        """
        data = request.json
        result, code = create_like(data)
        return result, code