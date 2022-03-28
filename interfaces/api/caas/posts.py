import logging

import werkzeug
from flask import request
from flask_restx import Resource, reqparse

from api.caas.functions import get_posts, create_user, get_users, create_post, get_comments, create_comment
from api.caas.serializers import users_input, users_output, posts_input, posts_output, commented_fields_output, commented_fields_input, posts_created, comments_created
from api.restplus import api

logger = logging.getLogger(__name__)

ns = api.namespace('posts', description='Operations related to posts management')


@ns.route('/')
class PostsCollection(Resource):
    @api.marshal_with(posts_output, as_list=True)
    def get(self):
        """
        Get a list of all posts.
        """
        posts = get_posts()
        return posts

    @api.expect(posts_input)
    @api.response(201, 'Post creation initiated', posts_created)
    def post(self):
        """
        Create a Post
        """
        data = request.json
        result, code = create_post(data)
        return result, code

