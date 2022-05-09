from tokenize import String
from mongoengine import *
from datetime import datetime

class Info(Document):
    title = StringField(max_length=200, required=True)
    description = StringField()
    create_date = DateField(default=datetime.now)
    modified_date = DateTimeField()


class Comments(Document):
    client = ImageField(required=True)
    date = DateField(default=datetime.now)
    body = StringField(max_length=200) 
    # parent_comment = Inte
