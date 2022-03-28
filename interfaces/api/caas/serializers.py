
from flask_restx import fields
from api.restplus import api

commented_fields_input = api.model('comments_input',{
    'create_date': fields.DateTime(required=True, dt_format='iso8601'),
    'created_by': fields.String(required=True, description='User Id who have commented that post'),
    'posted_on': fields.String(required=True, description='Post Id on which comment to be posted'),
    'description':fields.String(required=True, description='Comment description'),
})

commented_fields_output = api.model('comments_output',{
    'create_date': fields.DateTime(required=True, dt_format='iso8601'),
    'uuid': fields.String(required=True, description='UUID for a comment'),
    'created_by': fields.String(required=True, description='User Id who have commented that post'),
    'posted_on': fields.String(required=True, description='Post Id on which comment to be posted'),
    'likes': fields.Integer(required=False, description='Number of likes on comment'),
    'description':fields.String(required=True, description='Comment description'),
})

comments_created = api.model('comments_created',{
    'create_date': fields.DateTime(required=True, dt_format='iso8601'),
    'uuid': fields.String(required=True, description='UUID for a post'),
    'description':fields.String(required=True, description='Post description'),
    'created_by': fields.String(required=True, description='User Id who have created that post'),
    'posted_on': fields.String(required=True, description='Post Id on which comment to be posted'),
})

posts_input = api.model('posts_input',{
    # 'create_date': fields.DateTime(required=True, dt_format='iso8601'),
    'description':fields.String(required=True, description='Post description'),
    'created_by': fields.String(required=True, description='User Id who have created that post'),
})
posts_created = api.model('posts_created',{
    'create_date': fields.DateTime(required=True),
    'uuid': fields.String(required=True, description='UUID for a post'),
    'description':fields.String(required=True, description='Post description'),
    'created_by': fields.String(required=True, description='User Id who have created that post'),
})
posts_output = api.model('posts_output',{
    'create_date': fields.DateTime(required=True, dt_format='iso8601'),
    'uuid': fields.String(required=True, description='UUID for a post'),
    'description':fields.String(required=True, description='Post description'),
    'created_by': fields.String(required=True, description='User Id who have created that post'),
    'likes': fields.Integer(required=False, description='Number of likes'),
    'comments': fields.Nested(commented_fields_output, as_list=True),
})

users_output = api.model('user_output',{
    'uuid': fields.String(required=True, description='UUID of a user'),
    'name': fields.String(required=True, description='Name of a user'),
    'posts': fields.List(fields.String, required=False, description="List UUID of posts created by user"),
    'comments': fields.List(fields.String,required=False, description="List UUID of comments created by user"),
})
users_input = api.model('user_input',{
    'name': fields.String(required=True, description='Name of a user'),
    'password': fields.String(required=True, description='Password of a user'),
})


likes_input = api.model('likes_input',{
    'created_by': fields.String(required=True, description='User Id who have liked that post'),
    'comment_or_post': fields.String(required=True, description='Whether liked comment or post values needed COMMENT|POST'),
    'liked_id': fields.String(required=True, description='Post Id or comment id which should be liked'),
})

likes_output = api.model('likes_output',{
    'created_by': fields.String(required=True, description='User Id who have liked that post'),
    'comment_or_post': fields.String(required=True, description='Whether liked comment or post values needed COMMENT|POST'),
    'liked_id': fields.String(required=True, description='Post Id or comment id which should be liked'),
})