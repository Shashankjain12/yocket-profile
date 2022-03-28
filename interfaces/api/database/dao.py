import uuid, json, os, logging
from datetime import datetime, timezone
from mongoengine import connect

from api.database.model import Posts, Users, Comments
from xaas.config import Config as config

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

class MongoDao:

    def __init__(self):
        pass


    # ===================
    # Posts
    # ===================

    def getAllPosts(self, filters=None):
        posts = Posts.objects()
        if (len(posts) == 0):
            return []
        r = list()
        for n in posts:
            str_create_date = n.create_date.isoformat()
            print(str_create_date)
            _n = json.loads(n.to_json())
            _n['create_date'] = str_create_date
            r.append(_n)
        return r
    
    def createPost(self, data):
        uuid1 = str(uuid.uuid1())
        try:
            user = Users.objects.get(uuid = data['created_by'])
        except Users.DoesNotExist:
            user = None
            return user, 404
        if user:
            post = Posts(uuid=uuid1, create_date=datetime.now(), description = data['description'], created_by = data['created_by'])
            post.save()
            user.posts.append(post.uuid)
            user.save()
            _postDict = json.loads(post.to_json())
            if '_id' in _postDict:
                del _postDict['_id']
            return _postDict, 201
        else:
            return 'User not found', 404

    # ==========================
    # Users
    # ==========================
    def createUser(self, data):
        uuid1 = str(uuid.uuid1())
        try:
            users = Users.objects.get(name=data['name'])
        except Users.DoesNotExist:
            users = None
        if not users:
            user = Users(uuid=uuid1, name=data['name'], password = data['password'])
            if 'comments' in data:
                user.comments.append(data['comments'])
            if 'posts' in data:
                user.posts.append(data['posts'])
            user.save()
            _userDict = json.loads(user.to_json())
            if '_id' in _userDict:
                del _userDict['_id']
            if "password" in _userDict:
                del _userDict['password']
            return _userDict, 201
        else:
            return 'User already exists', 402

    def getAllUsers(self, filters=None):
        users = Users.objects()
        if (len(users) == 0):
            return []
        r = list()
        for n in users:
            _n = json.loads(n.to_json())
            r.append(_n)
        return r
    # ==========================
    # Comments
    # ==========================
    def getAllCommentsByPost(self, uuid, filters=None):
        post = Posts.objects.get(uuid = uuid)
        comments = post.comments
        if (len(comments) == 0):
            return []
        r = list()
        for n in comments:
            str_create_date = n.create_date.isoformat()
            _n = json.loads(n.to_json())
            _n['create_date'] = str_create_date
            r.append(_n)
        return r

    def createComments(self, data):
        uuid1 = str(uuid.uuid1())
        try:
            user = Users.objects.get(uuid = data['created_by'])
        except Users.DoesNotExist:
            user = None
            return user, 404
        try:
            post = Posts.objects.get(uuid = data['posted_on'])
        except Posts.DoesNotExist:
            post = None
            return post, 404
        if user and post:
            comment = Comments(uuid=uuid1, create_date=data['create_date'], description = data['description'], created_by = data['created_by'], posted_on = data['posted_on'])
            user.comments.append(comment.uuid)
            user.save()
            post.comments.append(comment)
            post.save()
            _commentDict = json.loads(comment.to_json())
            if '_id' in _commentDict:
                del _commentDict['_id']
            return _commentDict, 201
        else:
            return 'User or post not found', 404

    # ==========================
    # Likes
    # ==========================

    def createLike(self, data):
        try:
            user = Users.objects.get(uuid = data['created_by'])
        except Users.DoesNotExist:
            user = None
            return user, 404
        if data['comment_or_post'] == 'POST':
            try:
                post = Posts.objects.get(uuid = data['liked_id'])
            except Posts.DoesNotExist:
                post = None
                return post, 404
            if post.likes:
                flag_liked = 0
                for liked_post in user.liked_posts:
                    if post.uuid == liked_post:
                        flag_liked = 1
                        break
                if flag_liked == 1:
                    user.liked_posts.remove(post.uuid)
                    user.save()
                    post.likes -=1
                if flag_liked == 0:
                    user.liked_posts.append(post.uuid)
                    user.save()
                    post.likes +=1
            else:
                user.liked_posts.append(post.uuid)
                user.save()
                post.likes = 1
            post.save()
            _postDict = json.loads(post.to_json())
            if '_id' in _postDict:
                del _postDict['_id']
            return _postDict, 201

                    
        if data['comment_or_post'] == 'COMMENT':
            try:
                post = Posts.objects.get(comments__uuid = data['liked_id'])
                post = Posts.objects.get(uuid = post.uuid)
            except Posts.DoesNotExist:
                post = None
                return post, 404
            flag = 0
            for comment in post.comments:
                if comment.uuid == data['liked_id']:
                    flag = 1
                    if comment.likes:
                        comment_flag = 0
                        for liked_comment in user.liked_comments:
                            if comment.uuid == liked_comment:
                                comment_flag = 1
                                break
                        if comment_flag == 1:
                            user.liked_comments.remove(comment.uuid)
                            user.save()
                            comment.likes -=1
                        if comment_flag == 0:
                            user.liked_comments.append(comment.uuid)
                            user.save()
                            comment.likes +=1
                    else:
                        user.liked_comments.append(comment.uuid)
                        user.save()
                        comment.likes = 1
                    post.save()
                    _postDict = json.loads(post.to_json())
                    if '_id' in _postDict:
                        del _postDict['_id']
                    return _postDict, 201
            if flag == 0:
                return None, 404


            


            
                
            
