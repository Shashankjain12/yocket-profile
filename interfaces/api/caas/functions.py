import os, logging, werkzeug, yaml, json

from api.database.dao import MongoDao
from api.database.connection import Connection
from xaas.config import Config as config
from api.database.model import Posts
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

dao = MongoDao()


    
def get_posts():
    posts = None
    with Connection():
        posts = dao.getAllPosts()

    if (posts is None):
        return None, 404
    else:
        return posts, 200

def create_post(data):
    if not data['description']:
        return "Sorry post requires a description", 401 
    with Connection():
        result, code = dao.createPost(data)
    return result, code

def create_like(data):
    with Connection():
        result, code = dao.createLike(data)
    return result, code
    
    
def get_comments(uuid):
    comments = None
    with Connection():
        comments = dao.getAllCommentsByPost(uuid)
    if (comments is None):
        return None, 404
    else:
        return comments, 200

def create_comment(data):
    if not data['description']:
        return "Sorry comment requires a description", 401 
    with Connection():
        result, code = dao.createComments(data)
    return result, code
    
    
def get_users():
    users = None
    with Connection():
        users = dao.getAllUsers()

    if (users is None):
        return None, 404
    else:
        return users, 200

def create_user(data):
    if not data['name'] or not data['password']:
        return "Sorry needed name and password", 401 
    with Connection():
        result, code = dao.createUser(data)
    return result, code

