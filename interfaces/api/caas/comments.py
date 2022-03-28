import logging

import werkzeug
from flask import request
from flask_restx import Resource, reqparse

from api.caas.functions import get_posts, create_user, get_users, create_post, get_comments, create_comment
from api.caas.serializers import users_input, users_output, posts_input, posts_output, commented_fields_output, commented_fields_input, posts_created, comments_created
from api.restplus import api

logger = logging.getLogger(__name__)

ns = api.namespace('comments', description='Operations related to comments management')


@ns.route('/<string:uuid>')
class CommentsByIdCollection(Resource):
    @api.marshal_with(commented_fields_output, as_list=True)
    def get(self, uuid):
        """
        Get a list of all comments by post id.
        """
        comments = get_comments(uuid)
        return comments

@ns.route('/')
class CommentsCollecttion(Resource):
    @api.expect(commented_fields_input)
    @api.response(201, 'Comment creation initiated', comments_created)
    def post(self):
        """
        Create a Comment
        """
        data = request.json
        result, code = create_comment(data)
        return result, code
