from mongoengine import Document, \
    StringField, \
    ListField, \
    BooleanField, \
    EmbeddedDocumentField, \
    EmbeddedDocument, \
    EmbeddedDocumentListField, \
    IntField, \
    DateTimeField

from datetime import datetime, timezone

from mongoengine.fields import DictField

class Comments(EmbeddedDocument):
    uuid = StringField(max_length=48, required=False)
    create_date = DateTimeField(default=datetime.utcnow(), required=True)
    description = StringField(max_length=500, required=True)
    created_by = StringField(max_length=48, required=True)
    posted_on = StringField(max_length=48, required=True)
    likes = IntField(required=False)
    
    
    def __str__(self):
        _str = f"uuid: {self.uuid}, description: {self.description}, likes: \
        {self.likes}, created by:{self.created_by}"
        return _str

class Users(Document):
    uuid = StringField(max_length=48, required=False)
    name =  StringField(max_length=20, required=True)
    password = StringField(max_length=20, required=True)
    comments = ListField(StringField(), required=False)
    posts = ListField(StringField(), required=False)
    liked_posts = ListField(StringField(), required=False)
    liked_comments = ListField(StringField(), required=False)


class Posts(Document):
    create_date = DateTimeField(default=datetime.utcnow(), required=True)
    uuid = StringField(max_length=48, required=False)
    description = StringField(max_length=500, required=True)
    likes = IntField(required=False)
    comments = ListField(EmbeddedDocumentField(Comments))
    created_by = StringField(max_length=48, required=True)
    

    def __str__(self):
        _str = f"uuid: {self.uuid}, description: {self.description}, likes: \
        {self.likes}, created by:{self.created_by}"
        return _str
